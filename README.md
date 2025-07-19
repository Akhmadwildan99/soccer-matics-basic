# SoccerMathic

A Python project for soccer data analysis and visualization using StatsBomb open data and mplsoccer.

## Project Structure

- `pitch.py`: Basic pitch visualization
- `statsbomb/`: StatsBomb data analysis scripts
  - `init.py`: Initialize and explore StatsBomb competition data
  - `load_matches.py`: Load match data from specific competitions
  - `match.py`: Match analysis and statistics
  - `visualize_match.py`: Visualize shots from matches
- `ploting_shots/`: Shot visualization scripts
  - `plot_shot_on_one_half.py`: Plot shots on half pitch

## Setup

1. Create a virtual environment:
```
python -m venv my_mplsoccer_env
```

2. Activate the environment:
```
source my_mplsoccer_env/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```
pip install matplotlib mplsoccer pandas numpy
```

## Usage

Run any script using Python:
```
python statsbomb/visualize_match.py
```

## Data Source

This project uses the free StatsBomb open data available through the mplsoccer package.