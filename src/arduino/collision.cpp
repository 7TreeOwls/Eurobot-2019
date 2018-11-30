
#include "collision.h"

namespace robot {

	Sensor *distance_sensors = nullptr;
	uint8_t distance_sensor_count = 0;
	bool are_distance_sensors_enabled = false;

	void set_distance_sensors(uint8_t count, Sensor *sensors) {
		distance_sensors = sensors;
		distance_sensor_count = count;
	}

	void check_distance_sensors() {
		if (!are_distance_sensors_enabled) return;
		if (!drive::is_moving) return;

		bool is_collision_detected = false;

		// check distance sensors in parallel
		for (Sensor *sensor = distance_sensors; sensor != distance_sensors + distance_sensor_count; ++sensor) {
			// ...
		}

		if (is_collision_detected) {
			int16_t distance = drive::get_average_distance_travelled();
			drive::reset();
			robot::send_message('c', distance);
		}
	}

	void enable_distance_sensors() {
		are_distance_sensors_enabled = true;
	}

	void disable_distance_sensors() {
		are_distance_sensors_enabled = false;
	}

}
