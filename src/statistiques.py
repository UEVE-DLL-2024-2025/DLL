"""
Module for tracking and managing game statistics.
"""
import time
import os
import json

class Statistiques:
    """
    Class for tracking and managing game statistics.
    """
    def __init__(self, fichier_stats='statistiques.json'):
        self.timer_started = False
        self.parties_gagnees = 0
        self.parties_perdues = 0
        self.temps_total = 0.0
        self.nombre_parties = 0
        self.timer_start = None
        self.fichier_stats = fichier_stats
        self.meilleurs_scores = []
        self.load_statistics()

    def load_statistics(self):
        """
        Load statistics from the JSON file.
        """
        if os.path.exists(self.fichier_stats):
            with open(self.fichier_stats, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.parties_gagnees = data.get('parties_gagnees', 0)
                self.parties_perdues = data.get('parties_perdues', 0)
                self.temps_total = data.get('temps_total', 0.0)
                self.meilleurs_scores = data.get('meilleurs_scores', [])
                self.nombre_parties = self.parties_gagnees + self.parties_perdues

    def start_timer(self):
        """
        Start the timer.
        """
        self.timer_start = time.time()
        self.timer_started = True
        print("Le timer a démarré.")

    def stop_timer(self):
        """
        Stop the timer.
        """
        if self.timer_start is not None:
            elapsed_time = time.time() - self.timer_start
            self.temps_total += elapsed_time
            self.timer_start = None
            return elapsed_time
        return 0

    def record_victory(self, elapsed_time):
        """
        Record a victory and update statistics.
        """
        self.parties_gagnees += 1
        self.nombre_parties += 1
        self.meilleurs_scores.append(elapsed_time)
        self.meilleurs_scores = sorted(self.meilleurs_scores)[:5]
        self.save_statistics()

    def record_loss(self):
        """
        Record a loss and update statistics.
        """
        self.parties_perdues += 1
        self.nombre_parties += 1
        self.save_statistics()

    def save_statistics(self):
        """
        Save the current statistics to the JSON file.
        """
        data = {
            'parties_gagnees': self.parties_gagnees,
            'parties_perdues': self.parties_perdues,
            'temps_total': self.temps_total,
            'meilleurs_scores': self.meilleurs_scores,
        }
        with open(self.fichier_stats, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def display_statistics(self):
        """
        Display the current statistics.
        """
        temps_moyen = self.temps_total / self.nombre_parties if self.nombre_parties > 0 else 0
        print(f"Parties gagnées: {self.parties_gagnees}")
        print(f"Parties perdues: {self.parties_perdues}")
        print(f"Temps total: {self.temps_total:.2f} secondes")
        print(f"Temps moyen par partie: {temps_moyen:.2f} secondes")
        self.display_best_scores() 

    def display_best_scores(self):
        print("Meilleurs temps (en secondes) :")
        for idx, score in enumerate(self.meilleurs_scores, start=1):
            print(f"{idx}. {score:.2f} s")
