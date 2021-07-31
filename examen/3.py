{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fc989ab8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from pymongo import MongoClient\n",
    "from bs4 import BeautifulSoup\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ed8073ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "client =MongoClient(\"mongodb://localhost:27017\")\n",
    "db = client.comercio\n",
    "collection = db.web"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ae31c5d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "page = requests.get(\"https://www.elcomercio.com/\")\n",
    "soup = BeautifulSoup(page.content, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "b9b6d982",
   "metadata": {},
   "outputs": [],
   "source": [
    "article_content  = soup.find_all('p', class_= 'article-highlighted__description')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "baa2d7f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "extracted = []\n",
    "for article in article_content:\n",
    "    extracted.append({\n",
    "        'article' : article.get_text()\n",
    "    })"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "9c869282",
   "metadata": {},
   "outputs": [],
   "source": [
    "for post in extracted:\n",
    "    collection.insert_one(post)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "873359ca",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
