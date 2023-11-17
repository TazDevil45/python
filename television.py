class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Initializes a Television object as turned off, not muted,
        # at the minimum volume and the minimum channel
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        # Turns the TV On if it is Off and Off if it is On
        self.__status = not self.__status

    def mute(self):
        # Mutes the TV if it is Unmuted and Unmutes the TV if it is Muted
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        # Increases the Channel by 1 if the TV is not at the Max Channel
        # and goes to the Minimum Channel if the TV is at the Max Channel
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        # Decreases the Channel by 1 if the TV is not at the Minimum Channel
        # and goes to the Max Channel if the TV is at the Minimum Channel
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        # Increases the volume by 1 unless the TV is at Max Volume
        # in which case it doesn't change the volume
        if self.__status:
            self.__muted = False
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def volume_down(self):
        # Decreases the volume by 1 unless the TV is at Minimum
        # Volume in which case it doesn't change the volume
        if self.__status:
            self.__muted = False
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def __str__(self):
        # Returns a string telling whether the tv is on or off, what the channel
        # is and what the volume is (the volume is 0 if the TV is muted)
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
