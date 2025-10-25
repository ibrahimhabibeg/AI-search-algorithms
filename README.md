# AI Search Algorithms

This repo contains implementations for AI search algorithms including A\* and Dijkstra's.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/ibrahimhabibeg/AI-search-algorithms
   cd AI-search-algorithms
   ```

2. Install the required packages:
   ```bash
   uv sync
   ```

## Usage

The file `problem.py` includes abstract classes for defining search problems. You can create your own problem by inheriting from these classes.

Such a problem can be found in `n_queens.py`, which implements the N-Queens problem.

The file `search.py` contains a generic implementation of the best-first search algorithm, A\*, and Dijkstra's algorithm. They can be applied on any problem defined using the abstract classes in `problem.py`.
