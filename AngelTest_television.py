
from television import Television

def test_power_on_off():
    tv = Television()
    assert not tv.power(), "Initial power status should be off"
    tv.power()
    assert tv.power(), "Power status should be on after toggling"

def test_channel_up_down():
    tv = Television()
    tv.power() 
    initial_channel = tv.channel()
    tv.channel_up()
    assert tv.channel() != initial_channel, "Channel should change after channel_up"

    tv.channel_down()
    assert tv.channel() == initial_channel, "Channel should return to initial value after channel_down"

def test_volume_up_down():
    tv = Television()
    tv.power()  
    initial_volume = tv.volume()
    tv.volume_up()
    assert tv.volume() != initial_volume, "Volume should increase after volume_up"

    tv.volume_down()
    assert tv.volume() == initial_volume, "Volume should return to initial value after volume_down"

def test_mute():
    tv = Television()
    tv.power()  
    tv.mute()
    assert tv.is_muted(), "TV should be muted"

    tv.mute()
    assert not tv.is_muted(), "TV should be unmuted"



