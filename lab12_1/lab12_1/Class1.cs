using System;
using System.Threading;

namespace lab12_1
{
    public class AlarmClock
    {
        public delegate void AlarmEventHandler();
        public event AlarmEventHandler RaiseAlarm;

        private TimeSpan userTime;

        public AlarmClock(TimeSpan time)
        {
            userTime = time;
        }

        public void Start()
        {
            while (true)
            {
                TimeSpan currentTime = DateTime.Now.TimeOfDay;
                if (currentTime.Hours == userTime.Hours &&
                    currentTime.Minutes == userTime.Minutes &&
                    currentTime.Seconds == userTime.Seconds)
                {
                    RaiseAlarm?.Invoke();
                    break;
                }
                Thread.Sleep(1000);
            }
        }
    }
}
