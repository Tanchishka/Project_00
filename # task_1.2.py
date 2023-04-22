{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyOyfrHIlRnKs6pcZNgaDp03",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Tanchishka/Project_00/blob/main/Untitled10.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SKsx6oSqPFVY",
        "outputId": "969f83f6-5850-4239-af5e-f989a90bfb5b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Три песни звучат 11.71 минут\n"
          ]
        }
      ],
      "source": [
        "# task_1.2.py\n",
        "import random\n",
        "my_favorite_songs = [\n",
        "    ['Waste a Moment', 3.03],\n",
        "    ['New Salvation', 4.02],\n",
        "    ['Staying\\' Alive', 3.40],\n",
        "    ['Out of Touch', 3.03],\n",
        "    ['A Sorta Fairytale', 5.28],\n",
        "    ['Easy', 4.15],\n",
        "    ['Beautiful Day', 4.04],\n",
        "    ['Nowhere to Run', 2.58],\n",
        "    ['In This World', 4.02],\n",
        "]\n",
        "y = my_favorite_songs [0] [1], my_favorite_songs [1] [1], my_favorite_songs [2] [1], my_favorite_songs [3] [1], my_favorite_songs [4] [1], my_favorite_songs [5] [1], my_favorite_songs [6] [1], my_favorite_songs [7] [1], my_favorite_songs [8] [1]\n",
        "\n",
        "sampling = sum(random.choices(y, k=3))\n",
        "print(\"Три песни звучат {} минут\".format(sampling))\n"
      ]
    }
  ]
}
