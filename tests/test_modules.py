from modules.autonomous_agent import AutonomousAgent


def test_autonomous_agent():
    agent = AutonomousAgent()
    assert agent.act('I am happy') == 'encourage'

