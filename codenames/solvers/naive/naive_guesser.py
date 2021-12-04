import logging

from gensim.models import KeyedVectors

from codenames.game import PASS_GUESS, Board, Guess, Guesser, GuesserGameState
from language_data.model_loader import load_language

log = logging.getLogger(__name__)


class NaiveGuesser(Guesser):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.model: KeyedVectors = None  # type: ignore

    def on_game_start(self, language: str, board: Board):
        self.model = load_language(language=language)  # type: ignore

    def guess(self, game_state: GuesserGameState) -> Guess:
        if game_state.bonus_given:
            log.debug("Naive guesser does not take bonuses.")
            return Guess(PASS_GUESS)
        optional_words = [card.formatted_word for card in game_state.board.unrevealed_cards]
        current_hint_word = game_state.current_hint.formatted_word
        guess_word = self.model.most_similar_to_given(current_hint_word, optional_words)
        log.debug(f"Naive guesser thinks '{current_hint_word}' means '{guess_word}'.")
        guess_idx = game_state.board.find_card_index(guess_word)
        guess = Guess(card_index=guess_idx)
        return guess
