{
    "metadata": {
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
            "version": "3.8.5-final"
        },
        "orig_nbformat": 2,
        "kernelspec": {
            "name": "python3",
            "display_name": "Python 3",
            "language": "python"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2,
    "cells": [
        {
            "cell_type": "code",
            "execution_count": 3,
            "metadata": {},
            "outputs": [],
            "source": [
                "my_file = open(\"number.txt\", \"w\")\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 21,
            "metadata": {},
            "outputs": [],
            "source": [
                "my_file = open(\"number.txt\", \"w\")\n",
                "\n",
                "for i in range(10):\n",
                "    my_file.write(str(i))\n",
                "    my_file.write(\"\\n\")\n",
                "\n",
                "my_file.close()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 232,
            "metadata": {},
            "outputs": [
                {
                    "output_type": "execute_result",
                    "data": {
                        "text/plain": [
                            "2"
                        ]
                    },
                    "metadata": {},
                    "execution_count": 232
                }
            ],
            "source": [
                "my_file = open(\"number.txt\", \"w\")\n",
                "\n",
                "user_input1 = (input(\"Input 1st number:\"))\n",
                "\n",
                "my_file.write(user_input1)\n",
                "\n",
                "user_input2 = (input(\"Input 2nd number:\"))\n",
                "\n",
                "my_file.write(user_input2)\n",
                "\n",
                "user_input3 = (input(\"Input 3rd number:\"))\n",
                "\n",
                "my_file.write(user_input3)\n",
                "\n",
                "user_input4 = (input(\"Input 4th number:\"))\n",
                "\n",
                "my_file.write(user_input4)\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 199,
            "metadata": {},
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "Invalid input.\n"
                    ]
                }
            ],
            "source": [
                "def mark_grade_function(grade):\n",
                "    print(grade + \"Well done!\")\n",
                "\n",
                "mark = int(input(\"Enter the student's mark:\"))\n",
                "\n",
                "if mark <60:\n",
                "   print(\"F\")\n",
                "elif user_input >60 and mark <70:\n",
                "   print(\"C\")\n",
                "elif mark >70 and mark <80:\n",
                "   print(\"B\")\n",
                "elif mark >80 and mark <90:\n",
                "   print(\"A\")\n",
                "elif mark >90 and mark <101:\n",
                "   print(\"A*\")\n",
                "else:\n",
                "   print(\"Invalid input.\")\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 219,
            "metadata": {},
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "Your grade is C and your target grade is  70\nWell done!!\n"
                    ]
                }
            ],
            "source": [
                "def mark_grade_function(grade):\n",
                "    print(grade + \"Well done!\")\n",
                "\n",
                "mark = int(input(\"Enter the student's mark:\"))\n",
                "target_grade = int(input(\"What is your target grade?\"))\n",
                "\n",
                "if mark <60:\n",
                "   print(\"Your grade is F and your target grade is \", + target_grade)\n",
                "elif mark >=60 and mark <=69:\n",
                "   print(\"Your grade is C and your target grade is \", + target_grade)\n",
                "elif mark >=70 and mark <=79:\n",
                "   print(\"Your grade is B and your target grade is \", + target_grade) \n",
                "elif mark >=80 and mark <=89:\n",
                "   print(\"Your grade is A and your target grade is \", + target_grade)\n",
                "elif mark >=90 and mark <=100:\n",
                "   print(\"Your grade is A* and your target grade is \", + target_grade)\n",
                "else:\n",
                "   print(\"Invalid input.\")\n",
                "\n",
                "if target_grade > mark:\n",
                "   print(\"Almost there!\")\n",
                "    \n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 222,
            "metadata": {},
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "Your grade is C and your target grade is  60\n"
                    ]
                }
            ],
            "source": [
                "def mark_grade_function(grade):\n",
                "    print(grade + \"Well done!\")\n",
                "\n",
                "mark = int(input(\"Enter the student's mark:\"))\n",
                "target_grade = int(input(\"What is your target grade?\"))\n",
                "\n",
                "if mark <60:\n",
                "   print(\"Your grade is F and your target grade is \", + target_grade)\n",
                "elif mark >=60 and mark <=69:\n",
                "   print(\"Your grade is C and your target grade is \", + target_grade)\n",
                "elif mark >=70 and mark <=79:\n",
                "   print(\"Your grade is B and your target grade is \", + target_grade) \n",
                "elif mark >=80 and mark <=89:\n",
                "   print(\"Your grade is A and your target grade is \", + target_grade)\n",
                "elif mark >=90 and mark <=100:\n",
                "   print(\"Your grade is A* and your target grade is \", + target_grade)\n",
                "else:\n",
                "   print(\"Invalid input.\")\n",
                "\n",
                "if target_grade==mark:\n",
                "   print(\"Well done!You have reached your target!\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 224,
            "metadata": {},
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "Your grade is B and your target grade is  69\nWell done!\n"
                    ]
                }
            ],
            "source": [
                "def mark_grade_function(grade):\n",
                "    print(grade + \"Well done!\")\n",
                "\n",
                "mark = int(input(\"Enter the student's mark:\"))\n",
                "target_grade = int(input(\"What is your target grade?\"))\n",
                "\n",
                "if mark <60:\n",
                "   print(\"Your grade is F and your target grade is \", + target_grade)\n",
                "elif mark >=60 and mark <=69:\n",
                "   print(\"Your grade is C and your target grade is \", + target_grade)\n",
                "elif mark >=70 and mark <=79:\n",
                "   print(\"Your grade is B and your target grade is \", + target_grade) \n",
                "elif mark >=80 and mark <=89:\n",
                "   print(\"Your grade is A and your target grade is \", + target_grade)\n",
                "elif mark >=90 and mark <=100:\n",
                "   print(\"Your grade is A* and your target grade is \", + target_grade)\n",
                "else:\n",
                "   print(\"Invalid input.\")\n",
                "if target_grade < mark:\n",
                "   print(\"Well done!\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 227,
            "metadata": {},
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "[0 1 2 3 4 5 6 7 8 9]\n"
                    ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "array = np.array([0,1,2,3,4,5,6,7,8,9])\n",
                "\n",
                "print(array)\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 250,
            "metadata": {},
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "[[1 2 3]\n [4 5 6]\n [7 8 9]]\n"
                    ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "bool_arr = np.array([1,2,3,4,5,6,7,8,9])\n",
                "\n",
                "newArray = array.reshape(3, 3)\n",
                "\n",
                "print(newArray)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 253,
            "metadata": {},
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "[ 2  4  6  8 10]\n"
                    ]
                }
            ],
            "source": [
                "my_list2 = np.array([1,2,3,4,5])\n",
                "\n",
                "print(my_list2 + my_list2)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 270,
            "metadata": {},
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "[-1  2 -1  4 -1  6 -1  8 -1 10]\n"
                    ]
                }
            ],
            "source": [
                "import numpy as np \n",
                " \n",
                "v1 = np.arange(1, 11, 1)  \n",
                " \n",
                "v1[v1%2==1] = -1            \n",
                " \n",
                "print (v1)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 283,
            "metadata": {},
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "[[ 1  2  3  4  5]\n [ 6  7  8  9 10]]\n"
                    ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])\n",
                "\n",
                "newArray = array.reshape(2, 5) \n",
                "\n",
                "print(newArray)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 352,
            "metadata": {},
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "[1 2 3]\n"
                    ]
                }
            ],
            "source": [
                "a=np.arange(1,4)\n",
                "a\n",
                "array = ([1, 2, 3])\n",
                "a.reshape(3,1)\n",
                "array = ([[1],\n",
                "          [2],\n",
                "          [3]])\n",
                "np.vstack(a)\n",
                "array = ([[1],\n",
                "          [2],\n",
                "          [3]])\n",
                "\n",
                "print(a)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 345,
            "metadata": {},
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "[[0], [1], [2]]\n"
                    ]
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "np.arange(3)[:, np.newaxis]\n",
                "\n",
                "array = ([[0],\n",
                "         [1],\n",
                "         [2]])\n",
                "\n",
                "print(array)"
            ]
        }
    ]
}
