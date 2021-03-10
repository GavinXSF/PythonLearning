class Settings:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship settings.
        self.ship_limit = 3
        self.ship_speed = 1.5
        # Bullet settings.
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        # Alien settings.
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5
        # 1 -> moving right, -1 -> moving left
        self.fleet_direction = 1