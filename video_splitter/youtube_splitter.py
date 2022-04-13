
from copyreg import pickle
import json
import this
import networkx as nx
import cv2
import pafy
import pickle 



YOUTUBE_VIDEO_URL=""
VIDEO_FRAGMENT_SIZE=5

graph = nx.DiGraph()

class ding(object):
        

    def stream_video(self,context=None,publisher=None):
        
        # Imagine Dragons - Wrecked (eine guter lied)
        # url = "https://www.youtube.com/watch?v=hHZvUeAdzeI"
        
        # vPafy = pafy.new(url)

        video_id = 15#vPafy.videoid 

        # play = vPafy.getbest()

        # start the video play.url
        cap = cv2.VideoCapture(0)

        frame_count =200# = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
        start=0
        end = 0
        size = 0
        frames= []
        self.graph=nx.DiGraph()
        
        while (True):
            ret,frame = cap.read()
            size +=1
            end  +=1
            frames.append(frame)
            if size >= VIDEO_FRAGMENT_SIZE or size == frame_count:
                self.video_split(video_id,start,end,frames)
                # emptying the graph
                frames=[]
                print("emptying the graph")
                self.graph=nx.DiGraph()
                size = 0
                start = end

            cv2.imshow("frame",frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def video_split(self,id,start,end,frames):
        chunk = pickle.dumps(frames)
        # print(chunk)
        data = {
            "pickled_chunk":chunk
        }
        self.graph.add_nodes_from([(f"{id}-{start}-{end}",data)])
        print(self.graph.nodes())

ding().stream_video()