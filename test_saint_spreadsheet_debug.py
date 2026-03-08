import SPOCK.short_term_scheduler as SPOCKST
from astropy.time import Time

# ---- Short-term scheduler
schedule = SPOCKST.Schedules()
schedule.load_parameters()
schedule.day_of_night = Time('2026-01-09 15:00:00')
schedule.start_end_range = Time(['2026-01-10 01:54:00', '2026-01-10 03:22:00'])
schedule.observatory_name = 'Saint-Ex'
schedule.telescope = 'Saint-Ex'
#schedule.special_target(input_name="Trappist-1")
schedule.special_target_with_start_end(input_name="TOI-7522", use_Saint_Ex_spreadsheet=True)
schedule.make_scheduled_table()
schedule.planification()
schedule.make_night_block()