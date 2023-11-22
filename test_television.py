
from television import Television

def test_channel_up():
    tv = Television()
    tv.power()
    initial_channel = tv._Television__channel
    tv.channel_up()
    assert tv._Television__channel == initial_channel + 1
    tv._Television__channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv._Television__channel == Television.MIN_CHANNEL

def test_channel_down():
    tv = Television()
    tv.power()
    initial_channel = tv._Television__channel
    tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL
    tv._Television__channel = Television.MIN_CHANNEL + 1
    tv.channel_down()
    assert tv._Television__channel == initial_channel

def test_volume_up():
    tv = Television()
    tv.power()
    initial_volume = tv._Television__volume
    tv.volume_up()
    assert tv._Television__volume == initial_volume + 1
    tv._Television__volume = Television.MAX_VOLUME
    tv.volume_up()
    assert tv._Television__volume == Television.MAX_VOLUME

def test_volume_down():
    tv = Television()
    tv.power()
    initial_volume = tv._Television__volume
    tv.volume_down()
    assert tv._Television__volume == initial_volume - 1
    tv._Television__volume = Television.MIN_VOLUME
    tv.volume_down()
    assert tv._Television__volume == Television.MIN_VOLUME

