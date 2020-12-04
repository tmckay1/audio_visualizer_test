import numpy as np

"""
Instead of drawing the entire 2d plane, only draw out the wave which is the 
"""
def draw_points(strip, rgb, num_leds, p, prev_pixels, rgb_max):
    for i in range(num_leds ** 2):
        x = i % num_leds # for even y since we are in a snaking pattern
        y = i // num_leds

        # check if y is odd, in which case the x needs to change
        if y % 2 == 1:
            # we're snaked so the index of the rbg array is not exactly the mod of the current led position
            # instead it's the reflection of this point across the center of the number of leds
            x = num_leds - x - 1

        # Ignore pixels if they haven't changed (saves bandwidth)
        # if np.array_equal(p[:, x], prev_pixels[:, x]):
        #     continue

        max_level = int((rgb[x] / rgb_max) * num_leds) # the maximum level this wave form should reach
        should_draw = y <= max_level # only draw the pixel if it is at or below the maximum level, so we see a wave
        strip._led_data[i] = int(rgb[x]) if should_draw else 0