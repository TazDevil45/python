class Television:
    """
    A class representing details for a Television object
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, status=False, muted=False, volume=MIN_VOLUME, channel=MIN_CHANNEL) -> None:
        """
        Method that creates a Television object that starts turned off,
        not muted, a volume starting at 0, and a channel starting at 0
        """
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel

    def power(self) -> None:
        """
        Turns the TV On if it is Off and Off if it is On
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mutes the TV if it is Unmuted and Unmutes the TV if it is Muted
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increases the Channel by 1 if the TV is not at the Max Channel
        and goes to the Minimum Channel if the TV is at the Max Channel
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decreases the Channel by 1 if the TV is not at the Minimum Channel
        and goes to the Max Channel if the TV is at the Minimum Channel
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increases the volume by 1 unless the TV is at Max
        Volume in which case it doesn't change the volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by 1 unless the TV is at Minimum
        Volume in which case it doesn't change the volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to print the info about the Television object
        :return: A string with whether the TV is on or off and what channel and volume the TV is on
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
