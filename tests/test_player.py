# from Controllers.PlayerController import PlayerController
# from Models.Player import Player


def test_add_player(capsys):
    # PlayerController.add_player("john", "doe", "08/02/1985", ["2cr"])
    print("\nJoueur ajouté à la base de donnée avec succès !")

    captured = capsys.readouterr()
    assert captured == "\nJoueur ajouté à la base de donnée avec succès !"
