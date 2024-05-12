"""
Also know as pub/sub design pattern
"""


class WeatherPublisher:
    """
    Publisher
    """

    def __init__(self):
        self._subscribers = []
        self._temperature = 0

    def register_subscriber(self, subscriber):
        """
        Register an subscriber to receive temperature updates.
        """
        self._subscribers.append(subscriber)
        print(f"Registered {subscriber}")

    def remove_subscriber(self, subscriber):
        """
        Remove an subscriber from the subscription list.
        """
        self._subscribers.remove(subscriber)
        print(f"Removed {subscriber}")

    def notify_subscribers(self):
        """
        Notify all registered subscribers of the temperature change.
        """
        for subscriber in self._subscribers:
            subscriber.update_all(self._temperature)

    def set_temperature(self, temp):
        """
        Set the temperature and notify subscribers about the change.
        """
        self._temperature = temp
        print(f"WeatherStation: New temperature is {self._temperature}°C")
        self.notify_subscribers()


class TemperatureSubscriber:
    """
    Subscriber
    """

    def update_all(self, temp):
        print(f"Temperature subscribers: The current temperature is {temp}°C")


if __name__ == "__main__":
    # The client code

    # Create a weather station
    weather_publisher = WeatherPublisher()

    # Create temperature subscriber
    subscriberA = TemperatureSubscriber()
    subscriberB = TemperatureSubscriber()

    # Register subscriber to the weather station
    weather_publisher.register_subscriber(subscriberA)
    weather_publisher.register_subscriber(subscriberB)

    # Simulate changing weather conditions
    weather_publisher.set_temperature(23)
    weather_publisher.set_temperature(28)
