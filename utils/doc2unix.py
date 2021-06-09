{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Done. Saved 35156 bytes.\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "convert dos linefeeds (crlf) to unix (lf)\n",
    "usage: python dos2unix.py\n",
    "\"\"\"\n",
    "\n",
    "import sys\n",
    "\n",
    "original = 'word_data.pkl'\n",
    "destination = \"word_data_unix.pkl\"\n",
    "\n",
    "content = ''\n",
    "outsize = 0\n",
    "with open(original, 'rb') as infile:\n",
    "    content = infile.read()\n",
    "with open(destination, 'wb') as output:\n",
    "    for line in content.splitlines():\n",
    "        outsize += len(line) + 1\n",
    "        output.write(line + str.encode('\\n'))\n",
    "\n",
    "print(\"Done. Saved %s bytes.\" % (len(content)-outsize))"
   ]
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
