def get_hours_minutes_seconds(sec_amount: int) -> str:
    """
    Return the amount of hours, minutes, seconds from the given seconds amount.

    Params:
        sec_amount (int): Number of seconds to be converted in hours, minutes, seconds.
    """

    if sec_amount == 0:
        return '0s'

    hours, minutes = 0 ,0

    if sec_amount >= 3600:
        hours = sec_amount // 3600
        sec_amount = sec_amount - (hours * 3600)

    if sec_amount >= 60:
        minutes = sec_amount // 60
        sec_amount = sec_amount - (minutes * 60)

    to_join = []

    if hours:
        to_join.append(f"{str(hours)}h")

    if minutes:
        to_join.append(f"{str(minutes)}m")
    
    if sec_amount:
        to_join.append(f"{str(sec_amount)}s")

    return ' '.join(to_join)

if __name__ == "__main__":
    assert get_hours_minutes_seconds(30) == '30s'
    assert get_hours_minutes_seconds(60) == '1m'
    assert get_hours_minutes_seconds(90) == '1m 30s'
    assert get_hours_minutes_seconds(3600) == '1h'
    assert get_hours_minutes_seconds(3601) == '1h 1s'
    assert get_hours_minutes_seconds(3661) == '1h 1m 1s'
    assert get_hours_minutes_seconds(90042) == '25h 42s'
    assert get_hours_minutes_seconds(0) == '0s'