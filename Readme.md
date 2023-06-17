# MQTT Broker Script

This repository contains code files for creating a fake dataset of railways coming from IoT sensors. The script is configured to send the generated dataset to an MQTT broker (emqx).

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The MQTT Broker Script is designed to simulate railway data coming from IoT sensors. It generates a fake dataset that mimics the readings from various sensors deployed in railway systems. The generated data includes information such as temperature, humidity, speed, and location.

## Features

- Simulates railway data from IoT sensors.
- Generates a realistic fake dataset.
- Sends the generated dataset to an MQTT broker (emqx) for further processing or analysis.

## Prerequisites

Before using the MQTT Broker Script, ensure you have the following prerequisites:

- Python 3.6 or later installed on your system.
- Required Python dependencies, which can be installed using the provided `requirements.txt` file.

## Installation

To install and set up the MQTT Broker Script, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/PriyanshNegi/MQTT-Broker-Script.git
   ```

2. Navigate to the project directory:

   ```bash
   cd MQTT-Broker-Script
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the MQTT Broker Script, follow these steps:

1. Configure the MQTT broker connection details in the `config.py` file.
2. Customize the script settings and parameters as needed.
3. Run the script:

   ```bash
   python main.py
   ```

   This will start generating the fake dataset and publishing it to the configured MQTT broker.

4. Monitor the MQTT broker to receive the published dataset.

## Contributing

Contributions to the MQTT Broker Script are welcome! If you find any issues or have suggestions for improvement, please feel free to submit a pull request or create an issue in the repository.

## License

The MQTT Broker Script is open source and released under the [MIT License](LICENSE). You are free to modify, distribute, and use the code for personal and commercial purposes.

```

Feel free to modify the content as per your requirements and add any additional sections or details you deem necessary.