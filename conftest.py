# this is the conftest.py file


# below is an example of what the test should look like
# we need to import the function then do the def thing that must start with "test_"
# # this is the "test/game_test.py" file

# we also need to setup the main conditional in the code
#if __name__ == "__main__"
#everything that is not in the condition being tested should be in here

# from app.game import determine_winner


# def test_winning_choice():
#     assert determine_winner(user_choice="rock", computer_choice="paper") == "paper"
#     assert determine_winner(user_choice="rock", computer_choice="rock") == None
#     assert determine_winner(user_choice="rock", computer_choice="scissors") == "rock"

#     assert determine_winner(user_choice="paper", computer_choice="paper") == None
#     assert determine_winner(user_choice="paper", computer_choice="rock") == "paper"
#     assert determine_winner(user_choice="paper", computer_choice="scissors") == "scissors"

#     assert determine_winner(user_choice="scissors", computer_choice="paper") == "scissors"
#     assert determine_winner(user_choice="scissors", computer_choice="rock") == "rock"
#     assert determine_winner(user_choice="scissors", computer_choice="scissors") == None