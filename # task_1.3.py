{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyNZxYSI2nR3J2dGvHacimCH",
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
        "<a href=\"https://colab.research.google.com/github/Tanchishka/Project_00/blob/main/Untitled9.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "IJ7KCc6QNghy"
      },
      "outputs": [],
      "source": [
        "# task_1.3.py\n",
        "\n",
        "test_number = int(input(\"Число месяца 2023г. :\",))\n",
        "\n",
        "month31 = [1, 3, 5, 7, 8, 10, 11]\n",
        "month30 = [4, 6, 9, 12]\n",
        "month28 = [2]\n",
        "if test_number in month31:\n",
        "  print(\"Колличество дней в месяце: 31\")\n",
        "\n",
        "elif test_number in month28:\n",
        "  print(\"Колличество дней в месяце:28\")\n",
        "\n",
        "elif test_number in month30:\n",
        "  print(\"Колличество дней в месяце: 30\")\n",
        "else:\n",
        "  print(\"Месяца по таким номером не существует\")"
      ]
    }
  ]
}