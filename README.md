# Snake-Spiel mit Pygame

Dies ist eine Python-Implementierung des klassischen Snake-Spiels mithilfe der Pygame-Bibliothek.

## Spielbeschreibung

Das Spiel besteht aus einem Schlangenobjekt, das der Spieler steuern kann, sowie einem zufällig platzierten Futter, das die Schlangenlänge erhöht, wenn es gefressen wird. Das Ziel des Spiels ist es, so lange wie möglich zu überleben, indem man die Schlange vor dem Zusammenstoß mit ihrem eigenen Körper bewahrt.

## Funktionen

- **Steuerung der Schlange:** Der Spieler kann die Schlange mit den Pfeiltasten (oben, unten, links, rechts) steuern, um sie in die entsprechende Richtung zu bewegen.
- **Punktzahl:** Der Spieler sammelt Punkte, indem er das Futter frisst. Die Punktzahl wird auf dem Bildschirm angezeigt.
- **Spielende:** Das Spiel endet, wenn die Schlange gegen ihren eigenen Körper stößt. Ein Bildschirm mit der Spielendemeldung, der erzielten Punktzahl und der Möglichkeit, das Spiel neu zu starten, wird angezeigt.
- **Neustart:** Der Spieler kann das Spiel durch Drücken der Eingabetaste neu starten, nachdem das Spiel beendet wurde.

## Anleitung zur Ausführung

1. Stelle sicher, dass du Python auf deinem Computer installiert hast.
2. Installiere die erforderliche Bibliothek Pygame, falls noch nicht geschehen: `pip install pygame`.
3. Öffne das Terminal und navigiere zum Verzeichnis, in dem sich die Datei `snake_game.py` befindet.
4. Führe das Spiel aus, indem du den Befehl `python snake_game.py` eingibst.
5. Steuere die Schlange mit den Pfeiltasten und versuche, so viele Punkte wie möglich zu sammeln!
