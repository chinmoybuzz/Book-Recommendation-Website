import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# def recom(books_user_likes):
# 	def get_title_from_index(index):
# 		return df[df.index == index]["Title"].values[0]

# 	def get_index_from_title(Title):
# 		return df[df.Title == Title]["index"].values[0]

# 	books = pd.read_csv(r"D:\Book_Recommender_System\Bookz.csv")
# 	books=books[:1000]
# 	df=books
# 	img=pd.read_csv(r"D:\Book_Recommender_System\Imagez.csv")


# 	features = ['Title','Author','Publisher']
# 	for feature in features:
# 		df[feature] = df[feature].fillna('')

# 	def combine_features(row):
# 		try:
# 			return row['Title'] +" "+row['Author']+" "+row['Publisher']
# 		except:
# 			print("Error:", row)

# 	df["combined_features"] = df.apply(combine_features,axis=1)

# #Create count matrix from this new combined column
# 	cv = CountVectorizer()
# 	count_matrix = cv.fit_transform(df["combined_features"])

# #Compute the Cosine Similarity based on the count_matrix
# 	cosine_sim = cosine_similarity(count_matrix) 

# #Get index of this book from its title
# 	books_index = get_index_from_title(books_user_likes)
# 	similar_books = list(enumerate(cosine_sim[books_index]))

# #Get a list of similar books in descending order of similarity score
# 	sorted_similar_books = sorted(similar_books,key=lambda x:x[1],reverse=True)

# # titles of first 50 books
# 	l=[]
# 	t=[]
# 	i=0
# 	for element in sorted_similar_books:
# 			l.append(get_title_from_index(element[0]))
# 			t.append(get_index_from_title(l[i]))
# 			i=i+1
# 			if i>9:
# 				break

# 	output=l
# 	index=t

# 	imgg=[]
# 	year=[]
# 	author=[]
# 	final_list=[]
# 	for i in index:
# 		imgg.append(img["Image-URL-M"][i-1])
# 		year.append(books["Year"][i-1])
# 		author.append(books["Author"][i-1])
# 	for i in range(len(index)):
# 		temp=[]
# 		temp.append(output[i])
# 		temp.append(imgg[i])
# 		temp.append(year[i])
# 		temp.append(author[i])
# 		final_list.append(temp)
# 	return final_list


def recom(books_user_likes):
    import os
    from Main import app
    
    def get_title_from_index(index):
        return df[df.index == index]["Title"].values[0]

    def get_index_from_title(Title):
        return df[df.Title == Title]["index"].values[0]

    print("Current working directory:", os.getcwd())
    print("Application root path:", app.root_path)
    
    # Try different possible paths
    possible_paths = [
        "Bookz.csv",  # Current directory
        os.path.join(app.root_path, "Bookz.csv"),  # Main package directory
        os.path.join(os.path.dirname(app.root_path), "Bookz.csv")  # Project root
    ]
    print("books")
    # Find the correct path for the CSV files
    for path in possible_paths:
        if os.path.exists(path):
            books_path = path
            img_path = path.replace("Bookz.csv", "Imagez.csv")
            break
    else:
        raise FileNotFoundError("Could not find Bookz.csv in any expected location")
   
    # Read the CSV files
    books = pd.read_csv(books_path)
    books = books[:1000]
    df = books
    img = pd.read_csv(img_path)

    # Process features
    features = ['Title', 'Author', 'Publisher']
    for feature in features:
        df[feature] = df[feature].fillna('')

    def combine_features(row):
        try:
            return row['Title'] + " " + row['Author'] + " " + row['Publisher']
        except:
            print("Error:", row)
            return ""

    df["combined_features"] = df.apply(combine_features, axis=1)

    # Create count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])

    # Compute Cosine Similarity
    cosine_sim = cosine_similarity(count_matrix) 

    try:
        # Get index of the input book
        books_index = get_index_from_title(books_user_likes)
        similar_books = list(enumerate(cosine_sim[books_index]))

        # Sort books by similarity
        sorted_similar_books = sorted(similar_books, key=lambda x:x[1], reverse=True)

        # Get top 10 similar books
        l = []
        t = []
        for i, element in enumerate(sorted_similar_books):
            if i >= 10:
                break
            l.append(get_title_from_index(element[0]))
            t.append(get_index_from_title(l[i]))

        output = l
        index = t

        # Prepare final list with details
        final_list = []
        for i in index:
            temp = [
                output[index.index(i)],
                img["Image-URL-M"][i-1],
                books["Year"][i-1],
                books["Author"][i-1]
            ]
            final_list.append(temp)
            
        return final_list
        
    except Exception as e:
        print(f"Error processing book recommendation: {str(e)}")
        raise

recom("c")

def bookdisp():
	books=pd.read_csv("Bookz.csv")
	img=pd.read_csv("Imagez.csv")

	title=[]
	imgg=[]
	year=[]
	author=[]
	finallist=[]

	r=np.random.randint(2,1000,10)

	for i in r:
		title.append(books["Title"][i-1])
		imgg.append(img["Image-URL-M"][i-1])
		year.append(books["Year"][i-1])
		author.append(books["Author"][i-1])

	for i in range(10):
		temp=[]
		temp.append(title[i])
		temp.append(imgg[i])
		temp.append(year[i])
		temp.append(author[i])
		finallist.append(temp)

	return finallist