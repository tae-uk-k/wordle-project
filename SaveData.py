import pickle

class saveData:
    def save_game_state(player_name, score):
        data = {
           'player_name': player_name,
           'score': score
           }
        with open('game_state.pkl', 'wb') as file:
            pickle.dump(data, file)
    def load_game_state(self):
        try:
            with open('game_state.pkl', 'rb') as file:
                data = pickle.load(file)
                return data['player_name'], data['score']
        except FileNotFoundError:
            return None, 0
    def start_game(self):
        player_name, score = self.load_game_state()

        if player_name is None:
            player_name = input("플레이어 이름을 입력하세요: ")

        print(f"안녕하세요, {player_name}! 현재 점수는 {score}점입니다.")
        #save_game_state(player_name, score)<-저장하는 코드 어디에 써야할ㄹ 지 몰라서 일단 주석처리함