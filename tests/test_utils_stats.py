from src.utils.stats_utils import mean, median, mode, variance, stdev, percentiles


def test_stats_basic():
    data = [1,2,3,4,5]
    assert mean(data) == 3
    assert median(data) == 3
    assert mode([1,1,2]) == 1
    assert round(variance(data), 6) == round(2.0, 6)
    assert round(stdev(data), 6) == round(2**0.5, 6)
    assert percentiles(data, [0,50,100]) == [1,3,5]
