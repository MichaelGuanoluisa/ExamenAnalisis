{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "39e87fc7",
   "metadata": {},
   "outputs": [],
   "source": [
    "from facebook_scraper import get_posts\n",
    "import json\n",
    "import time\n",
    "from pymongo import MongoClient"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "43ca82ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "client = MongoClient(\"mongodb://localhost:27017\")\n",
    "db = client.facebook\n",
    "collection = db.fb_posts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "df947a62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-12-58d8566e64b4>:25: DeprecationWarning: save is deprecated. Use insert_one or replace_one instead\n",
      "  collection.save(doc)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "guardado con exito\n",
      "2\n",
      "guardado con exito\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\micha\\appdata\\local\\programs\\python\\python39\\lib\\site-packages\\facebook_scraper\\facebook_scraper.py:440: UserWarning: Facebook served mbasic/noscript content unexpectedly on https://m.facebook.com/page_content_list_view/more/?page_id=728041220550969&start_cursor=%7B%22timeline_cursor%22:%22AQHRISyewNCn96NYb-PQO36ZAXi4SnH_odgsXfLGPYvmb6pFsy8eWo_imoMip1HqKEitL5M10Mq-0SORGIaxtRSrBlCNKPJe-QUdTu5JGJhfPZP4ySO2elTvCmKQ1ZWtN3Wp%22,%22timeline_section_cursor%22:null,%22has_next_page%22:true%7D&num_to_fetch=4&surface_type=posts_tab\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "guardado con exito\n",
      "4\n",
      "guardado con exito\n",
      "5\n",
      "guardado con exito\n",
      "6\n",
      "guardado con exito\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\micha\\appdata\\local\\programs\\python\\python39\\lib\\site-packages\\facebook_scraper\\facebook_scraper.py:440: UserWarning: Facebook served mbasic/noscript content unexpectedly on https://m.facebook.com/page_content_list_view/more/?page_id=728041220550969&start_cursor=%7B%22timeline_cursor%22:%22AQHRS-YCsUuhQ23se5zk2bkZlromqriTE2OnUqi-WmNGtIrc5ElihksETxyRL_AjjGVZ2sF4TJT5cose4JfO0VGRHtjI_If_qS0B010KUYNkYwvZKzxBBtODTu0Ock259w1v%22,%22timeline_section_cursor%22:null,%22has_next_page%22:true%7D&num_to_fetch=4&surface_type=posts_tab\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
      "guardado con exito\n",
      "8\n",
      "guardado con exito\n",
      "9\n",
      "guardado con exito\n",
      "10\n",
      "guardado con exito\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\micha\\appdata\\local\\programs\\python\\python39\\lib\\site-packages\\facebook_scraper\\facebook_scraper.py:440: UserWarning: Facebook served mbasic/noscript content unexpectedly on https://m.facebook.com/page_content_list_view/more/?page_id=728041220550969&start_cursor=%7B%22timeline_cursor%22:%22AQHRxZCYp8OUJyaBbD_EJfaiTr1xyeTXZPHMPY7drHmWs3wD1OgD0gHUKolgOmiqYd9H-D9u43XffRnSPjM5k0_Wg1W-SveU4BylahME5WPiIVSC0DyZLOUzO4G3e287k5Lq%22,%22timeline_section_cursor%22:null,%22has_next_page%22:true%7D&num_to_fetch=4&surface_type=posts_tab\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n",
      "guardado con exito\n",
      "12\n",
      "guardado con exito\n",
      "13\n",
      "guardado con exito\n",
      "14\n",
      "guardado con exito\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\micha\\appdata\\local\\programs\\python\\python39\\lib\\site-packages\\facebook_scraper\\facebook_scraper.py:440: UserWarning: Facebook served mbasic/noscript content unexpectedly on https://m.facebook.com/page_content_list_view/more/?page_id=728041220550969&start_cursor=%7B%22timeline_cursor%22:%22AQHRh1X-A3gwyh97Msv8EregNuRhnM9FIQhSbsNj--l4Yb6TAeymyTes7zvOOM_BviuK-oRNAcAwCwEa5vy9pLDcHru8B4t33xghHD_0yDNyyO8gOkhsNxD1qAeb0qQb3VpR%22,%22timeline_section_cursor%22:null,%22has_next_page%22:true%7D&num_to_fetch=4&surface_type=posts_tab\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n",
      "guardado con exito\n",
      "16\n",
      "guardado con exito\n",
      "17\n",
      "guardado con exito\n",
      "18\n",
      "guardado con exito\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\micha\\appdata\\local\\programs\\python\\python39\\lib\\site-packages\\facebook_scraper\\facebook_scraper.py:440: UserWarning: Facebook served mbasic/noscript content unexpectedly on https://m.facebook.com/page_content_list_view/more/?page_id=728041220550969&start_cursor=%7B%22timeline_cursor%22:%22AQHRICPC9pG2ficSHHz_AweUuOJnVIIiAnSQXnKQRjXylRqrOdIBjKlYvclUH7S-vC8YqdMThJYkL21VZWj7JFrP-7thedJypG1jMBMho3vHp-clC6KJxtPK43jd7Ic_DYXV%22,%22timeline_section_cursor%22:null,%22has_next_page%22:true%7D&num_to_fetch=4&surface_type=posts_tab\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "19\n",
      "guardado con exito\n",
      "20\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-12-58d8566e64b4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mi\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m     \u001b[0mtime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m     \u001b[0mid\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mpost\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'post_id'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "i=1\n",
    "for post in get_posts(\"olimpicos\",pages=1000,extra_info=True):\n",
    "    print(i)\n",
    "    i=i+1\n",
    "    time.sleep(5)\n",
    "    \n",
    "    id=post['post_id']\n",
    "    doc={}\n",
    "    \n",
    "    doc['id']=id\n",
    "    mydate=post['time']\n",
    "    \n",
    "    try:\n",
    "        doc['texto']=post['text']\n",
    "        doc['date']=mydate.timestamp()\n",
    "        doc['likes']=post['likes']\n",
    "        doc['comments']=post['comments']\n",
    "        doc['shares']=post['shares']\n",
    "        try:\n",
    "            doc['reactions']=post['reactions']\n",
    "        except:\n",
    "            doc['reactions']={}\n",
    "        \n",
    "        doc['post_url']=post['post_url']\n",
    "        collection.save(doc)\n",
    "        \n",
    "        print('guardado con exito')\n",
    "    except Exception as e:\n",
    "        print('no se pudo guardar:'+str(e))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63f55250",
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
