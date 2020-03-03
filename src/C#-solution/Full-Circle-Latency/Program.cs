using System;
using System.Diagnostics;
using System.IO.Ports;
using System.Threading;

namespace Full_Circle_Latency
{
    class Program
    {
        private const string _portname1 = "/dev/ttyACM0";
        private const string _portname2 = "/dev/ttyACM1";
        private const int _baudrate = 115200;
        private const Parity _parity = Parity.None;
        private const int _databits = 8;
        private const StopBits _stopBits = StopBits.One;

        private static SerialPort _port1;
        private static SerialPort _port2;
        
        private static Stopwatch _sw = new Stopwatch();
        private static object _stopwatchLock = new object();
        
        
        static void Main(string[] args)
        {

            CheckTimePrecision(); // Are we able to measure nanosecs?

            Thread receive = new Thread(Receive);
            receive.Start();
            
            Thread send = new Thread(Send);
            send.Start();

            receive.Join();
            send.Join();
        }

        static void CheckTimePrecision()
        {
            long frequency = Stopwatch.Frequency;
            Console.WriteLine("  Timer frequency in ticks per second = {0}",
                frequency);
            long nanoSecsPerTick = (1000L*1000L*1000L) / frequency;
            Console.WriteLine("  Timer is accurate within {0} microseconds", 
                nanoSecsPerTick);

            if (nanoSecsPerTick != 1)
            {
                throw new Exception("The computer running this program is not capable of measuring nano seconds");
            }
        }

        static void Receive()
        {
            using (_port2 = new SerialPort(_portname2, _baudrate, _parity, _databits, _stopBits))
            {
                Console.WriteLine("opening port2");
                _port2.NewLine = "\n"; // Make sure this is a line feed on linux + windows OS, instead of LF CR
                _port2.Handshake = Handshake.None;
                _port2.RtsEnable = false;
                _port2.DtrEnable = false;
                _port2.Open();
                Console.WriteLine("opened port2");
                Console.WriteLine("can read?: " + _port2.BaseStream.CanRead);
                Console.WriteLine("is open?: " + _port2.IsOpen);

                while (true)
                {
                    Console.WriteLine("try reading");
                    _port2.ReadTimeout = 5000;

                    // TODO: BUG: ReadLine() blocks forever.
                    string received = _port2.ReadLine();
                    Console.WriteLine(received);

                    lock (_stopwatchLock) // Critical section for using the stop watch
                    {
                        _sw.Stop();
                        Console.WriteLine("Time:" +_sw.ElapsedTicks);
                        _sw.Reset();
                    }
                    
                    Thread.Sleep(100);
                }
            }
        }

        static void Send()
        {
            using (_port1 = new SerialPort(_portname1, _baudrate, _parity, _databits, _stopBits))
            {
                _port1.Open();
            
                byte[] buffer = new byte[] { 0, 1 };
                bool sendZero = true;

                while (true)
                {
                    lock (_stopwatchLock) // Critical section for using the stop watch
                    {
                        _sw.Start(); // Start measuring the time when sending the digital signal                    
                    }
                
                
                    if (sendZero)
                    {
                        _port1.Write(buffer, 0, 1);
                        sendZero = false;
                    }
                    else
                    {
                        _port1.Write(buffer, 1, 1);
                        sendZero = true;
                    }
                
                    Thread.Sleep(1000);
                }
            }
        }
    }
}