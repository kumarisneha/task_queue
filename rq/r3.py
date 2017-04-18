from r1 import count_words_at_url
import r2
result = r2.q.enqueue(count_words_at_url, 'http://nvie.com')
