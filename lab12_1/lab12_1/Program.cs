using System;

namespace lab12_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter time in HH:MM:SS format:");
            string input = Console.ReadLine();

            if (TimeSpan.TryParse(input, out TimeSpan userTime))
            {
                AlarmClock alarmClock = new AlarmClock(userTime);
                AlarmSubscriber subscriber = new AlarmSubscriber();

                // Subscribe the event
                alarmClock.RaiseAlarm += subscriber.RingAlarm;

                Console.WriteLine("Waiting for alarm time...");
                alarmClock.Start();
            }
            else
            {
                Console.WriteLine("Invalid time format. Please use HH:MM:SS.");
            }
        }
    }
}
