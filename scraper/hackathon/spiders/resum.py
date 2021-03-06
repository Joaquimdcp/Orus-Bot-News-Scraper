from pyteaser import Summarize

#define a series of non important words.
nowords=['tag', 'tags', '', 'z', 'yo', 'ya', 'y', 'x', 'w', 'vuestros', 'vuestro', 'vuestras', 'vuestra', 'voy', 'vosotros', 'vosotras', 'vez', 'verdadero', 'verdadera', 'verdad', 'ver', 'veces', 'vaya', 'varios', 'varias', 'van', 'vamos', 'valor', 'vais', 'va', 'v', 'ustedes', 'usted', 'uso', 'usas', 'usar', 'usan', 'usamos', 'usais', 'usa', 'unos', 'uno', 'unas', 'una', 'un', 'ultimo', 'u', 't\xc3\xba', 'tuyos', 'tuyo', 'tuyas', 'tuya', 'tuvo', 'tus', 'tu', 'tres', 'trav\xc3\xa9s', 'trata', 'tras', 'trabajo', 'trabajas', 'trabajar', 'trabajan', 'trabajamos', 'trabajais', 'trabaja', 'total', 'todos', 'todo', 'todav\xc3\xada', 'todavia', 'todas', 'toda', 'tienen', 'tiene', 'tiempo', 'ti', 'tercera', 'ten\xc3\xada', 'tenido', 'tengo', 'tenga', 'tener', 'tenemos', 'teneis', 'tendr\xc3\xa1n', 'tendr\xc3\xa1', 'temprano', 'te', 'tarde', 'tanto', 'tan', 'tampoco', 'tambi\xc3\xa9n', 'tambien', 'tal', 't', 's\xc3\xb3lo', 's\xc3\xad', 's\xc3\xa9', 'suyo', 'suyas', 'suya', 'sus', 'supuesto', 'su', 'soyos', 'soy', 'son', 'somos', 'solos', 'solo', 'solas', 'solamente', 'sola', 'sois', 'sobre', 'sino', 'sin', 'siguiente', 'sigue', 'siete', 'siendo', 'siempre', 'sido', 'si', 'se\xc3\xb1al\xc3\xb3', 'ser\xc3\xada', 'ser\xc3\xa1n', 'ser\xc3\xa1', 'sera', 'ser', 'seis', 'seg\xc3\xban', 'segundo', 'segunda', 'segun', 'sean', 'sea', 'se', 'salvo', 'sabes', 'saber', 'saben', 'sabemos', 'sabeis', 'sabe', 's', 'respecto', 'repente', 'realiz\xc3\xb3', 'realizar', 'realizado', 'raras', 'r', 'qu\xc3\xa9', 'qui\xc3\xa9nes', 'qui\xc3\xa9n', 'quiz\xc3\xa1s', 'quiz\xc3\xa1', 'quizas', 'quiza', 'quiere', 'quienes', 'quien', 'queremos', 'qued\xc3\xb3', 'que', 'qeu', 'q', 'pues', 'puedo', 'pueden', 'puede', 'pueda', 'pudo', 'pr\xc3\xb3ximos', 'pr\xc3\xb3ximo', 'proximo', 'propios', 'propio', 'propias', 'propia', 'pronto', 'principalmente', 'primeros', 'primero', 'primera', 'primer', 'posible', 'porque', 'por', 'poner', 'podr\xc3\xadan', 'podr\xc3\xada', 'podr\xc3\xa1n', 'podr\xc3\xa1', 'podrias', 'podrian', 'podriamos', 'podriais', 'podria', 'poder', 'podemos', 'podeis', 'pocos', 'poco', 'pocas', 'poca', 'pesar', 'pero', 'peor', 'pa\xc3\xacs', 'pasado', 'pasada', 'partir', 'parte', 'parece', 'para', 'pais', 'p', 'otros', 'otro', 'otras', 'otra', 'os', 'ocho', 'o', 'nunca', 'nuevos', 'nuevo', 'nuevas', 'nueva', 'nuestros', 'nuestro', 'nuestras', 'nuestra', 'nosotros', 'nosotras', 'nos', 'no', 'ning\xc3\xban', 'ningunos', 'ninguno', 'ningunas', 'ninguna', 'ni', 'nadie', 'nada', 'n', 'm\xc3\xados', 'm\xc3\xado', 'm\xc3\xadas', 'm\xc3\xada', 'm\xc3\xad', 'm\xc3\xa1s', 'muy', 'muchos', 'mucho', 'muchas', 'mucha', 'momento', 'modo', 'mismos', 'mismo', 'mismas', 'misma', 'mis', 'mios', 'mio', 'mientras', 'mias', 'mia', 'mi', 'menudo', 'menos', 'mencion\xc3\xb3', 'mejor', 'medio', 'mediante', 'me', 'mayor', 'mas', 'manifest\xc3\xb3', 'manera', 'mal', 'm', 'lugar', 'luego', 'los', 'lo', 'llevar', 'lleva', 'lleg\xc3\xb3', 'les', 'lejos', 'le', 'las', 'largo', 'lado', 'la', 'l', 'k', 'junto', 'j', 'ir', 'intento', 'intentas', 'intentar', 'intentan', 'intentamos', 'intentais', 'intenta', 'inform\xc3\xb3', 'informo', 'indic\xc3\xb3', 'incluso', 'igual', 'i', 'hubo', 'hoy', 'horas', 'hizo', 'hicieron', 'hemos', 'hecho', 'he', 'haya', 'hay', 'hasta', 'han', 'hago', 'haciendo', 'hacia', 'haces', 'hacerlo', 'hacer', 'hacen', 'hacemos', 'haceis', 'hace', 'hab\xc3\xadan', 'hab\xc3\xada', 'habr\xc3\xa1', 'hablan', 'habla', 'habia', 'haber', 'ha', 'h', 'gueno', 'grandes', 'gran', 'general', 'g', 'fuimos', 'fui', 'fueron', 'fuera', 'fue', 'final', 'fin', 'f', 'expres\xc3\xb3', 'explic\xc3\xb3', 'existen', 'existe', 'excepto', 'ex', 'est\xc3\xa1n', 'est\xc3\xa1', 'estuvo', 'estoy', 'estos', 'esto', 'este', 'estas', 'estar\xc3\xa1', 'estar', 'estan', 'estamos', 'estais', 'estados', 'estado', 'estaban', 'estaba', 'esta', 'esos', 'eso', 'ese', 'esas', 'esa', 'es', 'eres', 'eras', 'eran', 'eramos', 'era', 'entre', 'entonces', 'enseguida', 'enfrente', 'encuentra', 'encima', 'en', 'empleo', 'empleas', 'emplear', 'emplean', 'empleais', 'embargo', 'ellos', 'ello', 'ellas', 'ella', 'el', 'ejemplo', 'e', 'd\xc3\xb3nde', 'd\xc3\xadas', 'd\xc3\xada', 'durante', 'dos', 'donde', 'dio', 'dijo', 'dijeron', 'diferentes', 'diferente', 'dieron', 'dicho', 'dicen', 'dice', 'dias', 'dia', 'detr\xc3\xa1s', 'detras', 'despu\xc3\xa9s', 'despues', 'despacio', 'desde', 'deprisa', 'dentro', 'dem\xc3\xa1s', 'demasiado', 'delante', 'del', 'dej\xc3\xb3', 'decir', 'debido', 'deben', 'debe', 'debajo', 'de', 'dar', 'dan', 'dado', 'da', 'd', 'c\xc3\xb3mo', 'cu\xc3\xa1ntos', 'cu\xc3\xa1nto', 'cu\xc3\xa1ntas', 'cu\xc3\xa1nta', 'cu\xc3\xa1ndo', 'cu\xc3\xa1les', 'cu\xc3\xa1l', 'cuenta', 'cuatro', 'cuantos', 'cuanto', 'cuantas', 'cuanta', 'cuando', 'cualquier', 'cuales', 'cual', 'creo', 'cosas', 'contra', 'contigo', 'consigues', 'consiguen', 'consigue', 'consigo', 'consider\xc3\xb3', 'considera', 'conseguir', 'conseguimos', 'conocer', 'conmigo', 'con', 'como', 'coment\xc3\xb3', 'claro', 'cinco', 'ciertos', 'cierto', 'ciertas', 'cierta', 'cerca', 'casi', 'cada', 'c', 'buenos', 'bueno', 'buenas', 'buena', 'buen', 'breve', 'bien', 'bastante', 'bajo', 'b', 'a\xc3\xban', 'a\xc3\xb1adi\xc3\xb3', 'ayer', 'aunque', 'aun', 'atras', 'as\xc3\xad', 'asi', 'asegur\xc3\xb3', 'arribaabajo', 'arriba', 'aqu\xc3\xad', 'aqu\xc3\xa9llos', 'aqu\xc3\xa9llas', 'aqu\xc3\xa9lla', 'aqu\xc3\xa9l', 'aqui', 'aquellos', 'aquello', 'aquellas', 'aquella', 'aquel', 'aproximadamente', 'apenas', 'antes', 'anterior', 'ante', 'anta\xc3\xb1o', 'antano', 'ampleamos', 'ambos', 'alrededor', 'all\xc3\xad', 'alli', 'alg\xc3\xban', 'algunos', 'alguno', 'algunas', 'alguna', 'algo', 'al', 'ah\xc3\xad', 'ahora', 'ahi', 'agreg\xc3\xb3', 'afirm\xc3\xb3', 'adrede', 'adem\xc3\xa1s', 'ademas', 'adelante', 'acuerdo', 'actualmente', 'a', 'zero', 'yourselves', 'yourself', 'yours', 'your', "you've", "you're", "you'll", "you'd", 'you', 'yet', 'yes', "wouldn't", 'would', 'wonder', "won't", 'without', 'within', 'with', 'wish', 'willing', 'will', 'why', 'whose', 'whom', 'whole', 'whoever', "who's", 'who', 'whither', 'while', 'which', 'whether', 'wherever', 'whereupon', 'wherein', 'whereby', 'whereas', 'whereafter', "where's", 'where', 'whenever', 'whence', 'when', 'whatever', "what's", 'what', "weren't", 'were', 'went', 'well', 'welcome', "we've", "we're", "we'll", "we'd", 'we', 'way', "wasn't", 'was', 'wants', 'want', 'vs', 'viz', 'via', 'very', 'various', 'value', 'uucp', 'usually', 'using', 'uses', 'useful', 'used', 'use', 'us', 'upon', 'up', 'unto', 'until', 'unlikely', 'unless', 'unfortunately', 'under', 'two', 'twice', 'trying', 'try', 'truly', 'tries', 'tried', 'towards', 'toward', 'took', 'too', 'together', 'to', 'thus', 'thru', 'throughout', 'through', 'three', 'though', 'those', 'thoroughly', 'thorough', 'this', 'third', 'think', "they've", "they're", "they'll", "they'd", 'they', 'these', 'thereupon', 'theres', 'therein', 'therefore', 'thereby', 'thereafter', "there's", 'there', 'thence', 'then', 'themselves', 'them', 'theirs', 'their', 'the', 'thats', "that's", 'that', 'thanx', 'thanks', 'thank', 'than', 'th', 'tends', 'tell', 'taken', 'take', "t's", 'sure', 'sup', 'such', 'sub', 'still', 'specifying', 'specify', 'specified', 'sorry', 'soon', 'somewhere', 'somewhat', 'sometimes', 'sometime', 'something', 'someone', 'somehow', 'somebody', 'some', 'so', 'six', 'since', "shouldn't", 'should', 'she', 'shall', 'several', 'seven', 'seriously', 'serious', 'sent', 'sensible', 'selves', 'self', 'seen', 'seems', 'seeming', 'seemed', 'seem', 'seeing', 'see', 'secondly', 'second', 'says', 'saying', 'say', 'saw', 'same', 'said', 'right', 'respectively', 'relatively', 'regards', 'regardless', 'regarding', 'reasonably', 'really', 're', 'rd', 'rather', 'qv', 'quite', 'provides', 'probably', 'presumably', 'possible', 'plus', 'please', 'placed', 'perhaps', 'per', 'particularly', 'particular', 'own', 'overall', 'over', 'outside', 'out', 'ourselves', 'ours', 'our', 'ought', 'otherwise', 'others', 'other', 'or', 'onto', 'only', 'ones', 'one', 'once', 'on', 'old', 'okay', 'ok', 'oh', 'often', 'off', 'of', 'obviously', 'nowhere', 'now', 'novel', 'nothing', 'not', 'normally', 'nor', 'noone', 'none', 'non', 'nobody', 'nine', 'next', 'new', 'nevertheless', 'never', 'neither', 'needs', 'need', 'necessary', 'nearly', 'near', 'nd', 'namely', 'name', 'myself', 'my', 'must', 'much', 'mostly', 'most', 'moreover', 'more', 'might', 'merely', 'meanwhile', 'mean', 'maybe', 'may', 'many', 'mainly', 'ltd', 'looks', 'looking', 'look', 'little', 'likely', 'liked', 'like', "let's", 'let', 'lest', 'less', 'least', 'latterly', 'latter', 'later', 'lately', 'last', 'known', 'knows', 'know', 'kept', 'keeps', 'keep', 'just', 'itself', 'its', "it's", "it'll", "it'd", 'it', "isn't", 'is', 'inward', 'into', 'instead', 'insofar', 'inner', 'indicates', 'indicated', 'indicate', 'indeed', 'inc', 'inasmuch', 'in', 'immediate', 'ignored', 'if', 'ie', "i've", "i'm", "i'll", "i'd", 'however', 'howbeit', 'how', 'hopefully', 'hither', 'his', 'himself', 'him', 'hi', 'herself', 'hers', 'hereupon', 'herein', 'hereby', 'hereafter', "here's", 'here', 'her', 'hence', 'help', 'hello', "he's", 'having', "haven't", 'have', "hasn't", 'has', 'hardly', 'happens', "hadn't", 'had', 'greetings', 'gotten', 'got', 'gone', 'going', 'goes', 'go', 'gives', 'given', 'getting', 'gets', 'get', 'furthermore', 'further', 'from', 'four', 'forth', 'formerly', 'former', 'for', 'follows', 'following', 'followed', 'five', 'first', 'fifth', 'few', 'far', 'except', 'example', 'exactly', 'everywhere', 'everything', 'everyone', 'everybody', 'every', 'ever', 'even', 'etc', 'et', 'especially', 'entirely', 'enough', 'elsewhere', 'else', 'either', 'eight', 'eg', 'edu', 'each', 'during', 'downwards', 'down', 'done', "don't", 'doing', "doesn't", 'does', 'do', 'different', "didn't", 'did', 'despite', 'described', 'definitely', 'currently', 'course', "couldn't", 'could', 'corresponding', 'contains', 'containing', 'contain', 'considering', 'consider', 'consequently', 'concerning', 'comes', 'come', 'com', 'co', 'clearly', 'changes', 'certainly', 'certain', 'causes', 'cause', 'cant', 'cannot', "can't", 'can', 'came', "c's", "c'mon", 'by', 'but', 'brief', 'both', 'beyond', 'between', 'better', 'best', 'besides', 'beside', 'below', 'believe', 'being', 'behind', 'beforehand', 'before', 'been', 'becoming', 'becomes', 'become', 'because', 'became', 'be', 'awfully', 'away', 'available', 'at', 'associated', 'asking', 'ask', 'aside', 'as', 'around', "aren't", 'are', 'appropriate', 'appreciate', 'appear', 'apart', 'anywhere', 'anyways', 'anyway', 'anything', 'anyone', 'anyhow', 'anybody', 'any', 'another', 'and', 'an', 'amongst', 'among', 'am', 'always', 'although', 'also', 'already', 'along', 'alone', 'almost', 'allows', 'allow', 'all', "ain't", 'against', 'again', 'afterwards', 'after', 'actually', 'across', 'accordingly', 'according', 'above', 'about', 'able', "a\'s"]

#define a series of unimportant symbols.
#print(points)
points = [',', ';', '\n', '.', ':', '!', '?', ' -', '-', '+', '\\', '&', '$', '#', '%', '*', '/', '"', "'", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def get_tags(texts):
    #joins title and text.
    text = ' '.join(texts)

    #elminate unimportant symbols.
    for sign in points:
        text = text.replace(sign, '')

        #eliminate double spaces.
    text.replace('  ', ' ')

    #separate the text in words.
    array = text.split(' ')

    #change all the words to lowercase.
    for i in range(len(array)):
        array[i] = array[i].lower()

    #store in a new vector each word an the times it is repeated.
    words = []
    while len(array)>0:
        word = array.pop()
        n = array.count(word)
        words.append([word, n+1])
        #once stored once we don't want to store it again.
        while True:
            try:
                array.remove(word)
            except:
                break

    #eliminate non important words from the stored ones.
    important = []
    while len(words)>0:
        word = words.pop()
        if word[0] in nowords or len(word[0])<3:
            pass
        else:
            important.append(word)

    #sort the remaining words by the amount of time they are repeated
    important.sort(key=lambda x: x[1])

    #define at most 5 tags from the words found.
    few = max(important[-1][1]/5, 2) #if the words don't appear at least this many times they are not relevant

    tags = []
    for i in range(len(important)):
        if (important[-i-1][1]<few):
            break
        tags.append(important[-i-1])

        #return the most relevant words found together with the times each word appears.
    return (tags)

#this function receives an array of arrays each of them containing a title and a text and returns an array of arrays each containing a relevant word and a summary of texts relevant to that word
def get_database(texts):
	tagsBig = []
	for text in texts:
		tagsBig.append(get_tags(text))

	tagsaux = []
	for tags in tagsBig:
		for tag in tags:
			tagsaux.append(tag)

	#we erase repeated tags.
	tagsSmall = []
	for tag in tagsaux:
		tagsSmall.append(tagsaux.pop())
		#erase from tagsaux the readen tag.
		while True:
			try:
				#look for element tag in array tagsaux
				i = tagsaux.index(tagsSmall[-1])
				tagsSmall[-1][1] += tagsaux[i][1]
				tagsaux.remove(tagsSmall[-1])
			except:
				break

	#sort from most important to least important tag.
	tagsSmall.sort(key=lambda x: -x[1])

	#get only the ten most relevant tags
	tagsSmall = tagsSmall[:10]

	#here we are going to put the tuples of tags and summaries.
	summarizedTags = []
	for tag in tagsSmall:

		#get the index of the text where tag[0] appears with the most frequency
		most = 0
		indexmost = 0
		for i in range(len(tagsBig)):
			for tagweight in tagsBig[i]:
				if (tagweight[0]==tag[0] and tagweight[1]>=most):
					indexmost = i
					most = tagweight[1]

		#get the index of the text where tag[0] appears with the most frequency
		second = -1
		indexsecond = 0
		for i in range(len(tagsBig)):
			if (i!=indexmost):
				for tagweight in tagsBig[i]:
					if (tagweight[0]==tag[0] and tagweight[1]>=second):
						indexsecond = i
						second = tagweight[1]

		if (second==-1):
			title = texts[indexmost][0]
			text = texts[indexmost][1]
		else:
			title = texts[indexmost][0]+' and '+texts[indexsecond][0]
			text = texts[indexmost][1]+'\n'+texts[indexsecond][1]

		#get the text.
		text = Summarize(title, text)[-1]
		try:
			#if possible makes another summary
			summarizedTags.append([tag[0], Summarize(title, text)[0]+'\n\n'+Summarize(title, text)[1]])
		except:
			#if not fuck it
			summarizedTags.append([tag[0], title+'\n\n'+text])

	#returns tags with summary
	return summarizedTags




#we define a function which attempts to return a sumup of a given text.
def get_sum_up(texts):
    text = ' '.join(texts)
    importantWords = get_tags([text])

    #divide by paragraphs
    paragraphs = text.split('\n')

    sumup = []
    for paragraph in paragraphs:
        sentences = paragraph.split('.')
        if len(sentences>2):
            sumup.append(sortSentence(sentences, importantWords))

    return '\n'.join(sumup)


def sortSentence(paragraph, importantWords):
    important = paragraph[0] #initialize the most important sentence.
    importance = sentenceImportance(paragraph[0], importantWords) #define the importance of the first sentence
    for sentence in paragraph:
        if (sentenceImportance(paragraph[0], importantWords)>importance):
            importance = sentenceImportance(paragraph[0], importantWords)
            important = sentence

    return important

def sentenceImportance(sentence, importantWords):
    importance = 0
    sentence = sentence.lower()
    for word in importantWords:
        if (word[0] in sentence):
            importance += word[1]

    return importance
