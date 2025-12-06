import socket
import threading
import json
import time

class GameServer:
    def __init__(self, host='0.0.0.0', port=5555):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        
        self.clients = {}
        self.players = {}
        self.lock = threading.Lock()
        self.running = True
        
        print(f"服务器启动，监听 {self.host}:{self.port}")
        
    def handle_client(self, conn, addr):
        print(f"新连接: {addr}")
        player_id = f"player_{len(self.clients) + 1}"
        
        with self.lock:
            self.clients[player_id] = conn
            self.players[player_id] = {
                'x': 0,
                'y': 0,
                'direction': 'down',
                'is_moving': False
            }
        
        try:
            while self.running:
                data = conn.recv(1024).decode()
                if not data:
                    break
                
                message = json.loads(data)
                
                with self.lock:
                    if player_id in self.players:
                        # 更新玩家状态
                        if 'x' in message:
                            self.players[player_id]['x'] = message['x']
                        if 'y' in message:
                            self.players[player_id]['y'] = message['y']
                        if 'direction' in message:
                            self.players[player_id]['direction'] = message['direction']
                        if 'is_moving' in message:
                            self.players[player_id]['is_moving'] = message['is_moving']
                
                # 发送所有玩家状态给所有客户端
                self.broadcast()
                
        except Exception as e:
            print(f"客户端错误 {addr}: {e}")
        finally:
            with self.lock:
                if player_id in self.clients:
                    del self.clients[player_id]
                if player_id in self.players:
                    del self.players[player_id]
            
            conn.close()
            print(f"连接关闭: {addr}")
            self.broadcast()
    
    def broadcast(self):
        with self.lock:
            game_state = {
                'players': self.players
            }
            message = json.dumps(game_state).encode()
            
            for client in list(self.clients.values()):
                try:
                    client.send(message)
                except:
                    pass
    
    def start(self):
        while self.running:
            try:
                conn, addr = self.server.accept()
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.daemon = True
                thread.start()
            except KeyboardInterrupt:
                self.running = False
                break
        
        self.server.close()
        print("服务器已关闭")

if __name__ == "__main__":
    server = GameServer()
    server.start()