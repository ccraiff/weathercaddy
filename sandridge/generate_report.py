import json
import sys

# Create the report structure
report = {
    "course": "Sand Ridge Disc Golf Course",
    "report_generated_at": "2026-03-27 22:24 EDT",
    "current_wind": {
        "speed_mph": 1.2,
        "direction_degrees": 22,
        "gusts_mph": 6.9,
        "description": "Light breeze from NNE"
    },
    "forecast_5hr": [
        {"time_edt": "2026-03-27 21:00 EDT", "speed_mph": 1.2, "direction_degrees": 22},
        {"time_edt": "2026-03-27 22:00 EDT", "speed_mph": 3.6, "direction_degrees": 338},
        {"time_edt": "2026-03-27 23:00 EDT", "speed_mph": 4.7, "direction_degrees": 325},
        {"time_edt": "2026-03-28 00:00 EDT", "speed_mph": 7.8, "direction_degrees": 321},
        {"time_edt": "2026-03-28 01:00 EDT", "speed_mph": 12.5, "direction_degrees": 336}
    ],
    "holes": []
}

# Add a few sample holes to demonstrate the structure
holes = []

# Hole 1
holes.append({
    "hole_number": 1,
    "hole_label": "Hole 1",
    "wind_info": {
        "azimuth_degrees": 84.3,
        "relative_degrees": 297.7,
        "clock_face": "10 o-clock",
        "description": "10 o-clock crosswind from left"
    },
    "tips_rh": {
        "bh": {
            "disc_recommendation": "Overstable driver",
            "shot_strategy": "With a 10 o'clock crosswind from the left on this 392ft par 3, your RHBH flight plate is exposed to the wind — throw a controlled RHFH with an overstable fairway driver to fight the rightward push while staying left of the roadway OB that runs along the entire right side of the fairway and past the basket."
        },
        "fh": {
            "disc_recommendation": "Overstable fairway driver",
            "shot_strategy": "For this 10 o'clock crosswind from the left on Hole 1, your RHFH is the safer choice as it keeps the flight plate away from the wind — use an overstable fairway driver on a slight hyzer line to maintain control over the 392ft distance while carefully avoiding the roadway OB that borders the entire right side of the fairway."
        }
    },
    "tips_lh": {
        "bh": {
            "disc_recommendation": "Overstable driver",
            "shot_strategy": "On Hole 1's 392ft par 3 with a 10 o'clock crosswind from the left, your LHBH fade right works with the wind pushing left — throw an overstable driver on a hyzer line to maximize distance while keeping your shot left of the roadway OB that runs along the entire right side of the fairway and past the basket."
        },
        "fh": {
            "disc_recommendation": "Overstable fairway driver",
            "shot_strategy": "For Hole 1's 10 o'clock crosswind from the left, your LHFH flight plate is exposed to the wind — use an overstable fairway driver with a controlled anhyzer release to fight the leftward push on this 392ft par 3 while staying well left of the roadway OB that borders the entire right side of the fairway."
        }
    }
})

# Add more holes here...

report["holes"] = holes

# Write to file
with open('report.json', 'w') as f:
    json.dump(report, f, indent=2)

print("Report generated with", len(holes), "holes")
