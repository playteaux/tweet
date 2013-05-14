import sys
import json

def hw(tweet_file, scores):
	count = 0
	for tweet in tweet_file:
		entry = json.loads(tweet)
		if 'text' in entry:
			count += 1
			msg = entry['text']
			words = msg.split()
			sscore = 0
			for word in words:
				if word in scores:
					sscore+=scores[word]
			print "%d:%f" %(count, sscore)	

def lines(fp):
    print str(len(fp.readlines()))

def build_affin_dict (fp,scores):	
	for line in fp:
		term, score = line.split("\t")
		scores[term] = int(score)

def main():
    scores = {}
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    build_affin_dict (sent_file,scores)
    hw(tweet_file, scores)
    lines(sent_file)
    lines(tweet_file)
    tweet_file.close()
    sent_file.close()

if __name__ == '__main__':
    main()
