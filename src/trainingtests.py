from snakeai import SnakeAI


def test_mutation_rates(): # Tests 1%, 2%, 3%, and 5% mutation rates
    ai = SnakeAI(0.01, "snakesPointCross1Percent.json",
                 "scoresPointCross1Percent.json")
    ai.train()

    ai = SnakeAI(0.02, "snakesPointCross2Percent.json",
                 "scoresPointCross2Percent.json")
    ai.train()

    ai = SnakeAI(0.03, "snakesPointCross3Percent.json",
                 "scoresPointCross3Percent.json")
    ai.train()

    ai = SnakeAI(0.05, "snakesPointCross5Percent.json",
                 "scoresPointCross5Percent.json")
    ai.train()


if __name__ == '__main__':
    test_mutation_rates()
