
import Data.List
import Data.Map (fromListWith, toList)

-- ty https://stackoverflow.com/questions/4978578/how-to-split-a-string-in-haskell
wordsWhen     :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'


-- ty https://stackoverflow.com/questions/7108559/how-to-find-the-frequency-of-characters-in-a-string-in-haskell
stringCharFreqs input = toList $ fromListWith (+) [(c, 1) | c <- input]


test_input = "32T3K 765\n\
\T55J5 684\n\
\KK677 28\n\
\KTJJT 220\n\
\QQQJA 483"


real_input = "JJJJ8 619\n\
\Q4J94 152\n\
\77587 277\n\
\7333J 651\n\
\QQQQ2 419\n\
\72KA3 851\n\
\555Q2 806\n\
\37QTT 72\n\
\39446 597\n\
\KK99T 453\n\
\T5522 247\n\
\8TK48 109\n\
\46J82 146\n\
\444A7 788\n\
\Q9TQJ 116\n\
\3A9AA 529\n\
\5AAAJ 63\n\
\T9522 668\n\
\ATJTJ 879\n\
\7TATT 11\n\
\88686 885\n\
\5QJ55 782\n\
\72K77 576\n\
\KQ48J 352\n\
\JJ488 704\n\
\3K356 12\n\
\JQJAQ 201\n\
\26272 373\n\
\88JJ2 855\n\
\35333 167\n\
\755Q4 465\n\
\5J6T5 136\n\
\JTA23 477\n\
\J8488 252\n\
\55556 417\n\
\55T8T 193\n\
\22782 148\n\
\2372J 811\n\
\J4K72 114\n\
\9Q4KK 303\n\
\4J2J2 388\n\
\6AJ9Q 965\n\
\45335 952\n\
\982T3 184\n\
\55Q5Q 762\n\
\TK572 972\n\
\T5TT5 250\n\
\2Q8Q8 119\n\
\AA436 353\n\
\6KKK5 501\n\
\399J9 561\n\
\T8AA3 406\n\
\JKAAK 482\n\
\55585 695\n\
\KJTK7 559\n\
\27JJT 690\n\
\4QQQ4 990\n\
\J32J3 24\n\
\5J545 863\n\
\558QQ 920\n\
\49949 187\n\
\JQQK9 179\n\
\T29JK 605\n\
\699J6 445\n\
\KK7QJ 284\n\
\647AJ 509\n\
\KK8K3 893\n\
\7KK79 174\n\
\J8J55 523\n\
\6T3AQ 410\n\
\44349 296\n\
\JJJJJ 158\n\
\99998 570\n\
\5TKQ6 266\n\
\9933T 300\n\
\K665K 724\n\
\QTTTQ 807\n\
\7Q5Q5 375\n\
\Q6666 966\n\
\TQ35K 825\n\
\T5QQ5 18\n\
\KQ794 802\n\
\K42KT 240\n\
\QKKJJ 97\n\
\77647 504\n\
\87J84 443\n\
\KATTK 666\n\
\52J88 889\n\
\66JKJ 977\n\
\6AQ94 84\n\
\36A78 514\n\
\AA67A 286\n\
\74Q34 490\n\
\QQ8QQ 79\n\
\3K555 323\n\
\Q3JKT 338\n\
\2A222 448\n\
\935JJ 798\n\
\43QTJ 226\n\
\5TA7K 162\n\
\553QQ 420\n\
\QKKQ9 204\n\
\9399K 565\n\
\8T66T 638\n\
\4444Q 83\n\
\J2223 173\n\
\4T454 639\n\
\4K3K4 454\n\
\Q2255 955\n\
\965JJ 658\n\
\A48K3 409\n\
\JJA22 728\n\
\42242 677\n\
\AKT6J 155\n\
\77774 838\n\
\82AAA 894\n\
\22A6K 775\n\
\59377 235\n\
\6K86J 451\n\
\26AT6 671\n\
\8388J 47\n\
\JJ293 449\n\
\39333 500\n\
\62222 456\n\
\5K55Q 36\n\
\KKK77 773\n\
\QQ739 287\n\
\67686 588\n\
\53329 341\n\
\TQTTT 213\n\
\44224 796\n\
\AAAJA 222\n\
\6KK22 92\n\
\AJK2A 627\n\
\5T858 739\n\
\J6579 462\n\
\T3933 717\n\
\3AQ82 380\n\
\Q564Q 898\n\
\8QQQ7 470\n\
\93T29 317\n\
\64K67 867\n\
\JTTTT 299\n\
\4499J 714\n\
\6QQ76 435\n\
\AJ979 897\n\
\66KTK 594\n\
\2AA84 178\n\
\8858K 533\n\
\KKKKJ 689\n\
\99393 906\n\
\2A777 711\n\
\33Q78 540\n\
\55566 364\n\
\2AA3A 513\n\
\5KJKK 98\n\
\Q79T9 809\n\
\AKKKK 34\n\
\5932K 349\n\
\88858 198\n\
\52222 307\n\
\944T7 126\n\
\T36Q7 472\n\
\T4444 792\n\
\TTKJT 828\n\
\35652 580\n\
\ATQ79 94\n\
\ATJTA 518\n\
\3JT52 656\n\
\2TT23 438\n\
\9K497 630\n\
\AQ735 569\n\
\95997 175\n\
\27248 874\n\
\3AKJK 693\n\
\94979 709\n\
\2QQT2 137\n\
\4A598 253\n\
\33JQ2 520\n\
\8A747 457\n\
\K222A 720\n\
\89A99 87\n\
\T8TTA 706\n\
\Q489A 322\n\
\J4TT4 319\n\
\T5JTK 57\n\
\T7T97 280\n\
\A7A7A 471\n\
\9K583 91\n\
\77887 909\n\
\5JJ55 629\n\
\AJ434 901\n\
\JJ7A9 166\n\
\Q99J9 577\n\
\44T4T 688\n\
\T8J8K 759\n\
\5AJ5A 149\n\
\95599 890\n\
\3Q662 781\n\
\JAJ5A 940\n\
\TTJ3J 676\n\
\88976 203\n\
\4AA4Q 985\n\
\95T53 956\n\
\K3333 595\n\
\52555 544\n\
\AK942 684\n\
\2T548 415\n\
\K66J7 407\n\
\KT7T2 103\n\
\97973 14\n\
\43343 708\n\
\55Q53 422\n\
\A835K 616\n\
\TT589 236\n\
\6322K 186\n\
\A4K4A 866\n\
\2K563 861\n\
\5J255 591\n\
\Q9Q98 450\n\
\T7796 305\n\
\9K229 258\n\
\9A27J 993\n\
\5QKQJ 224\n\
\T5J5T 161\n\
\3TA3K 464\n\
\558A8 183\n\
\Q333Q 48\n\
\A5A55 771\n\
\34437 182\n\
\8KKKK 95\n\
\J5696 291\n\
\66K88 914\n\
\33489 661\n\
\KK2TT 498\n\
\59999 877\n\
\7TTTT 492\n\
\5J52K 531\n\
\398K6 783\n\
\99A9T 49\n\
\667TT 86\n\
\AAKK6 928\n\
\2626J 346\n\
\3J675 37\n\
\T8488 268\n\
\KK222 763\n\
\76666 749\n\
\47457 138\n\
\QTTT6 211\n\
\TTT8T 754\n\
\37754 652\n\
\2QK4K 770\n\
\3A3AA 988\n\
\KJ35A 779\n\
\434AA 962\n\
\44JJ4 519\n\
\K2QQQ 133\n\
\JJ77J 662\n\
\89899 292\n\
\AA9AA 10\n\
\3J3J3 329\n\
\477JJ 841\n\
\39Q33 609\n\
\8A26T 431\n\
\TK63J 641\n\
\57595 880\n\
\KQ7QJ 123\n\
\QJJK5 665\n\
\88AKA 566\n\
\73Q67 265\n\
\7673T 904\n\
\Q7Q2A 937\n\
\9223Q 991\n\
\T45A7 386\n\
\96J6A 220\n\
\QK748 859\n\
\QQAQ8 172\n\
\222K2 100\n\
\QQJ7Q 822\n\
\9AK3A 873\n\
\2766A 647\n\
\K4432 402\n\
\TKTTK 77\n\
\24423 915\n\
\J5423 853\n\
\32243 463\n\
\Q3QQQ 15\n\
\676T6 368\n\
\54555 378\n\
\AJ7A6 192\n\
\9J3JA 139\n\
\2TT3T 393\n\
\QT33A 503\n\
\56684 120\n\
\Q56Q2 786\n\
\K32AT 943\n\
\384A7 780\n\
\44Q4Q 117\n\
\6AJ54 214\n\
\9J9K9 189\n\
\7TKKT 808\n\
\34J8J 360\n\
\AAATA 755\n\
\JQJTA 705\n\
\T9T94 387\n\
\4J445 718\n\
\Q8Q8Q 6\n\
\T652J 745\n\
\Q9272 372\n\
\T9924 936\n\
\3J352 691\n\
\577T5 827\n\
\QQ344 596\n\
\29TTJ 310\n\
\2332T 752\n\
\66J66 217\n\
\999JJ 261\n\
\Q968T 857\n\
\5233K 165\n\
\3K3KA 489\n\
\33T3J 964\n\
\KT3TT 507\n\
\T88TT 244\n\
\55595 350\n\
\6944J 791\n\
\224AT 887\n\
\3447J 30\n\
\T2K86 169\n\
\Q23Q3 556\n\
\KK88K 602\n\
\4AAA6 534\n\
\ATA85 626\n\
\8J3KA 699\n\
\KKQKK 931\n\
\4TTTQ 328\n\
\A3684 923\n\
\62AA2 776\n\
\8464K 121\n\
\846K6 944\n\
\6J69J 610\n\
\KK55J 769\n\
\7TKQ2 358\n\
\TQ4TK 93\n\
\JK4A4 698\n\
\842J8 971\n\
\JJ222 129\n\
\8J32J 233\n\
\278K2 674\n\
\68Q8J 727\n\
\A663T 318\n\
\56A5A 64\n\
\7775Q 180\n\
\K568Q 846\n\
\9K8AA 279\n\
\AJTTK 196\n\
\JA254 151\n\
\5Q2A3 913\n\
\A8788 816\n\
\48729 267\n\
\QKQT4 572\n\
\Q4949 953\n\
\43KK3 125\n\
\83676 2\n\
\J9959 76\n\
\TJTT3 38\n\
\472T5 948\n\
\5T679 511\n\
\JJ52A 293\n\
\7TT99 649\n\
\47467 176\n\
\J3J5K 844\n\
\8KJKK 982\n\
\AAJJA 961\n\
\6K633 589\n\
\45Q96 208\n\
\6QQQJ 888\n\
\46464 701\n\
\T33JT 52\n\
\625J9 336\n\
\K84T2 20\n\
\54447 246\n\
\T8AT8 118\n\
\827A6 795\n\
\99967 274\n\
\TT44T 61\n\
\AA2KK 784\n\
\Q2AAT 276\n\
\KA9AA 478\n\
\3QJQK 452\n\
\A97JK 551\n\
\K4774 746\n\
\QKKTT 371\n\
\63834 369\n\
\QQ4QQ 163\n\
\54757 835\n\
\7Q436 919\n\
\3AA33 560\n\
\8Q288 546\n\
\99K99 74\n\
\QJ9QA 67\n\
\48888 404\n\
\4KQA3 850\n\
\36872 930\n\
\359T4 426\n\
\T6578 315\n\
\626T6 772\n\
\K79A9 599\n\
\4A9JA 653\n\
\366J6 45\n\
\2T8J7 628\n\
\TTTT3 967\n\
\A426J 202\n\
\QA6T2 760\n\
\7775A 73\n\
\488K7 16\n\
\KTTTT 644\n\
\84JA9 484\n\
\57775 232\n\
\KTQ8T 7\n\
\8JK88 681\n\
\5A5J8 733\n\
\66A66 228\n\
\K28A4 736\n\
\59647 682\n\
\4Q6A5 663\n\
\62226 578\n\
\5T489 26\n\
\6J65T 548\n\
\24725 9\n\
\K35TJ 314\n\
\26A68 455\n\
\JJTTT 907\n\
\AJ285 899\n\
\JQJQJ 927\n\
\QQTJQ 554\n\
\AT235 141\n\
\TJK9J 35\n\
\9666Q 499\n\
\66A76 999\n\
\86K94 947\n\
\495AT 632\n\
\TK385 403\n\
\993KK 530\n\
\38366 625\n\
\4J744 881\n\
\AA777 694\n\
\84994 248\n\
\46Q2A 39\n\
\TT6TJ 751\n\
\A55AA 741\n\
\2Q545 946\n\
\QT238 959\n\
\22A3A 845\n\
\6T9T7 710\n\
\KKJQK 856\n\
\888A8 722\n\
\3899J 239\n\
\969A9 365\n\
\A88A8 62\n\
\A77J7 945\n\
\Q6222 288\n\
\2QQ62 761\n\
\K22TQ 270\n\
\2JJJJ 421\n\
\KTTKJ 678\n\
\J32A7 787\n\
\58688 8\n\
\55499 814\n\
\KK7KK 425\n\
\9Q97K 82\n\
\53353 804\n\
\5KQJT 590\n\
\67677 963\n\
\K2A9K 747\n\
\A424A 926\n\
\AJ3T3 891\n\
\75A29 132\n\
\5994T 502\n\
\J8J5K 399\n\
\44JQQ 437\n\
\6AKQ9 670\n\
\JA376 905\n\
\KAKQA 110\n\
\464JA 908\n\
\88228 719\n\
\37773 558\n\
\555K5 27\n\
\KTT38 902\n\
\7J77J 821\n\
\T888T 13\n\
\J9K4T 497\n\
\7KJK5 738\n\
\7AKQ2 969\n\
\TQQQ5 785\n\
\5TAT2 849\n\
\JT5A5 143\n\
\QAAAQ 496\n\
\QQKKK 231\n\
\T77K7 488\n\
\77TTQ 461\n\
\TAQ69 535\n\
\43T47 933\n\
\8K3KJ 212\n\
\768QQ 573\n\
\A75A5 643\n\
\88JT4 130\n\
\J2QQ2 444\n\
\KT788 515\n\
\22922 75\n\
\73TJ5 379\n\
\75555 25\n\
\27666 408\n\
\J4J3T 41\n\
\94Q57 525\n\
\A85A5 273\n\
\66386 526\n\
\J98KK 618\n\
\A6A64 234\n\
\2KK2K 147\n\
\3KKKK 636\n\
\88JJ8 495\n\
\T5T55 58\n\
\Q959J 734\n\
\9J292 508\n\
\686J8 376\n\
\A5862 309\n\
\J9T3T 875\n\
\9Q99Q 22\n\
\T773Q 970\n\
\Q3QT6 424\n\
\4455A 466\n\
\77443 469\n\
\49999 405\n\
\Q65AA 655\n\
\TA576 840\n\
\A9999 96\n\
\AA9J9 256\n\
\5999K 941\n\
\28338 423\n\
\797KT 581\n\
\5K55K 819\n\
\7A3KK 613\n\
\7Q77K 434\n\
\KK686 102\n\
\76755 257\n\
\Q4429 185\n\
\922K2 712\n\
\AA4AA 842\n\
\A2AJA 326\n\
\78A3T 40\n\
\T2Q2T 483\n\
\47A7A 249\n\
\54558 703\n\
\6972Q 522\n\
\AJ689 586\n\
\Q3Q5J 669\n\
\5KK65 262\n\
\2A2AA 847\n\
\A62Q7 737\n\
\2KT2K 645\n\
\4K4TJ 929\n\
\AK993 794\n\
\48576 839\n\
\T4683 604\n\
\Q3556 686\n\
\67Q2K 871\n\
\AA665 370\n\
\Q66Q9 925\n\
\J77Q7 660\n\
\TJAA7 374\n\
\TT6TA 574\n\
\AJJ4A 414\n\
\3TK28 337\n\
\95AKT 864\n\
\777J9 541\n\
\67979 171\n\
\8888J 829\n\
\5QJQ5 345\n\
\884J4 225\n\
\JQK6T 106\n\
\6K6KJ 367\n\
\333A6 89\n\
\59939 506\n\
\4J525 642\n\
\6A765 624\n\
\A282J 852\n\
\2QJQQ 107\n\
\K8822 70\n\
\67KQA 316\n\
\7J8TQ 111\n\
\5555J 837\n\
\42TQ7 112\n\
\J2J55 886\n\
\2Q9QJ 942\n\
\ATATT 778\n\
\7J676 304\n\
\5K8T7 269\n\
\9KJA2 275\n\
\36TJ3 324\n\
\QJ954 976\n\
\58353 960\n\
\59436 42\n\
\AA444 188\n\
\3A333 834\n\
\JK695 973\n\
\39383 394\n\
\A5566 17\n\
\55533 975\n\
\49448 742\n\
\A8KJK 486\n\
\QQQJ9 524\n\
\73T5Q 65\n\
\8T265 441\n\
\44774 206\n\
\8J329 633\n\
\5555Q 823\n\
\76962 195\n\
\2QQTT 648\n\
\KAQ4Q 882\n\
\6K9A3 312\n\
\62JT8 860\n\
\AKAA5 381\n\
\8888K 216\n\
\66622 4\n\
\76JTJ 884\n\
\KKK2K 343\n\
\2A345 685\n\
\J922A 440\n\
\2AAAA 487\n\
\K49K5 391\n\
\74QJ2 984\n\
\4777Q 750\n\
\76676 553\n\
\5A829 995\n\
\32K22 584\n\
\J89Q5 181\n\
\66663 646\n\
\J4857 335\n\
\66462 623\n\
\36A63 593\n\
\T2Q72 620\n\
\44244 330\n\
\QJ4A7 512\n\
\8J8T8 227\n\
\7ATA7 290\n\
\3A993 325\n\
\QQ2Q2 229\n\
\KKQ5Q 134\n\
\KA658 389\n\
\QQ94Q 467\n\
\5636J 592\n\
\49494 59\n\
\27272 460\n\
\T8T98 536\n\
\T2TTJ 215\n\
\TJQ4Q 68\n\
\5J5JJ 321\n\
\48A79 910\n\
\8465J 954\n\
\K734A 71\n\
\9QJ33 101\n\
\AQAJQ 177\n\
\777J7 401\n\
\K9TTT 1\n\
\8A394 532\n\
\7TTJT 748\n\
\AQT7J 355\n\
\J547T 735\n\
\8882K 398\n\
\33773 916\n\
\J7477 294\n\
\5QQQ5 935\n\
\9K9T9 50\n\
\45554 606\n\
\J44JA 427\n\
\6A494 731\n\
\KQK5T 521\n\
\77447 331\n\
\43J33 543\n\
\8592Q 468\n\
\Q62TJ 430\n\
\99AA9 687\n\
\J26J6 283\n\
\J7697 587\n\
\44J44 716\n\
\7K7K7 90\n\
\9KJ49 723\n\
\72724 475\n\
\AA77J 831\n\
\33363 621\n\
\Q3QJQ 306\n\
\66QQQ 744\n\
\9AT23 207\n\
\22733 713\n\
\TA67T 883\n\
\4447K 892\n\
\9JA99 598\n\
\45646 69\n\
\58225 537\n\
\TJTT9 797\n\
\JQJQQ 978\n\
\66T6A 219\n\
\TT6TT 124\n\
\J484Q 344\n\
\TQ32A 836\n\
\6J6J6 29\n\
\97J9J 979\n\
\6J266 622\n\
\AJ96T 218\n\
\72KKK 298\n\
\2A7A2 243\n\
\TJJ7T 758\n\
\8K682 974\n\
\25QKA 411\n\
\QQQ24 862\n\
\56667 245\n\
\56QQQ 43\n\
\477J4 481\n\
\Q7A5J 555\n\
\45T54 545\n\
\TAQQQ 989\n\
\7AAAA 766\n\
\6Q852 951\n\
\84Q39 458\n\
\JKJ42 730\n\
\AT376 313\n\
\2J427 108\n\
\9TQJ6 429\n\
\444AJ 150\n\
\7TQJT 479\n\
\QQJQQ 127\n\
\2K534 547\n\
\A888Q 272\n\
\JAA65 66\n\
\88585 600\n\
\Q92Q9 528\n\
\7TTA7 725\n\
\3JQT8 160\n\
\444A3 800\n\
\J5558 878\n\
\JQ5K6 608\n\
\827Q3 122\n\
\J9999 607\n\
\KJQ69 140\n\
\K368J 99\n\
\5T777 721\n\
\K6665 582\n\
\2666A 683\n\
\6668J 817\n\
\79779 221\n\
\JQ9Q5 474\n\
\J9996 692\n\
\66J76 396\n\
\53577 732\n\
\JATAA 803\n\
\3KJK6 447\n\
\3K37K 439\n\
\TQQT3 1000\n\
\62A64 416\n\
\78295 571\n\
\33334 726\n\
\J7999 896\n\
\98988 493\n\
\5AQ5J 153\n\
\4QJ44 320\n\
\4JQQQ 168\n\
\55252 385\n\
\33388 615\n\
\29292 679\n\
\2QAKK 327\n\
\48848 702\n\
\4J3T8 476\n\
\QT332 869\n\
\35899 53\n\
\29A9A 308\n\
\77722 777\n\
\685T5 824\n\
\2242J 238\n\
\66QKJ 131\n\
\6K38Q 397\n\
\5K798 400\n\
\A9JK6 793\n\
\255A2 51\n\
\33TTT 557\n\
\6Q6Q6 311\n\
\Q4687 957\n\
\KK67K 820\n\
\T56A3 432\n\
\75A8J 200\n\
\696J6 78\n\
\94954 382\n\
\2Q89J 356\n\
\35A3A 56\n\
\9J977 575\n\
\A65K2 550\n\
\J6367 32\n\
\27222 194\n\
\KAAKA 348\n\
\AAAA3 395\n\
\TJ7T7 715\n\
\T3Q92 433\n\
\AQ99Q 843\n\
\79957 263\n\
\9899K 986\n\
\64Q26 801\n\
\34A4Q 922\n\
\J3838 567\n\
\QQQ5Q 667\n\
\JT732 347\n\
\A8QAT 872\n\
\43T7K 413\n\
\4Q445 362\n\
\34T44 491\n\
\A33A7 932\n\
\22T47 340\n\
\25224 281\n\
\K97Q2 485\n\
\77577 949\n\
\466J6 637\n\
\88868 868\n\
\22822 996\n\
\3AAA4 302\n\
\86J8J 997\n\
\Q24Q2 983\n\
\4224T 357\n\
\T9254 826\n\
\Q2777 980\n\
\K5KKA 28\n\
\K8K88 654\n\
\89432 494\n\
\333J3 538\n\
\79T46 428\n\
\25252 255\n\
\TT8T9 998\n\
\425AA 157\n\
\29TAQ 145\n\
\877K7 60\n\
\558Q3 631\n\
\62665 542\n\
\Q5948 442\n\
\683JQ 197\n\
\49483 697\n\
\3K35K 938\n\
\8TT47 601\n\
\44JAT 568\n\
\T29Q4 33\n\
\AKJ9K 264\n\
\7AAA4 549\n\
\T47A6 241\n\
\27A33 3\n\
\3AA3K 260\n\
\6AK9K 516\n\
\9AJ85 113\n\
\K4454 767\n\
\Q63JJ 764\n\
\4AJK2 958\n\
\66266 278\n\
\74869 994\n\
\8KTK8 768\n\
\73A63 19\n\
\A7285 813\n\
\TA9J4 657\n\
\JTQKT 209\n\
\J7A55 88\n\
\JAA9A 480\n\
\77282 950\n\
\98J88 359\n\
\7K2K2 753\n\
\44494 700\n\
\K9J6T 918\n\
\KJ74J 282\n\
\QKQK4 640\n\
\T6669 743\n\
\A3QAQ 31\n\
\74AAJ 611\n\
\595J9 757\n\
\5JA59 392\n\
\78878 334\n\
\T4TTT 799\n\
\77678 21\n\
\33KKK 832\n\
\7787J 740\n\
\KAKKA 170\n\
\7KQ3Q 870\n\
\KK9K3 858\n\
\63JJ4 351\n\
\T65J9 199\n\
\37895 412\n\
\9J9A8 833\n\
\K3KJ5 765\n\
\785T2 259\n\
\Q3Q38 564\n\
\JJQJA 446\n\
\Q7JK3 527\n\
\QKK86 634\n\
\4653K 812\n\
\3JK78 815\n\
\J2255 242\n\
\95A52 789\n\
\93539 254\n\
\5K6Q4 205\n\
\444KK 142\n\
\57K75 191\n\
\3T887 154\n\
\JA685 612\n\
\TA9J8 104\n\
\36847 517\n\
\KJQQK 583\n\
\22J2A 865\n\
\66343 774\n\
\44884 128\n\
\779Q9 934\n\
\T3476 790\n\
\4A446 510\n\
\A8AAA 384\n\
\666AJ 390\n\
\64347 921\n\
\QJ8KA 418\n\
\JJQ6T 563\n\
\J4236 23\n\
\AJJ37 339\n\
\44448 271\n\
\Q6K96 297\n\
\57J55 115\n\
\TTK8K 729\n\
\666AA 377\n\
\24662 251\n\
\4TAAA 135\n\
\83353 659\n\
\2J429 354\n\
\9K9K9 756\n\
\AQQQQ 459\n\
\45445 301\n\
\A775J 912\n\
\38333 237\n\
\T3T88 680\n\
\9Q2Q3 190\n\
\268K3 164\n\
\868Q7 987\n\
\66466 44\n\
\QJJKQ 818\n\
\T48KQ 854\n\
\526J6 363\n\
\69666 295\n\
\55KAA 895\n\
\K75Q4 144\n\
\TKKKA 332\n\
\98699 650\n\
\78828 848\n\
\KT45K 617\n\
\275TA 992\n\
\J38QA 635\n\
\TKA3K 579\n\
\4Q4Q5 672\n\
\7377T 614\n\
\KT5J7 675\n\
\QA8TJ 903\n\
\2Q66Q 539\n\
\44J46 917\n\
\4K539 968\n\
\3654Q 55\n\
\A33J7 505\n\
\23959 924\n\
\T25JK 664\n\
\33Q88 911\n\
\Q6677 333\n\
\9669K 289\n\
\9782A 81\n\
\66699 876\n\
\6ATAK 552\n\
\87772 223\n\
\5T555 366\n\
\9KK9K 900\n\
\55666 673\n\
\77KKT 105\n\
\55358 156\n\
\AA4AJ 342\n\
\22TJ2 436\n\
\8A448 361\n\
\4KKK4 80\n\
\84J7Q 805\n\
\ATQTJ 473\n\
\K92JQ 707\n\
\222J2 981\n\
\KQ7J7 603\n\
\55JJA 46\n\
\QKJAA 696\n\
\842K5 562\n\
\K58K8 5\n\
\T9T5T 939\n\
\TT956 230\n\
\53555 810\n\
\JK8K8 585\n\
\J795A 85\n\
\4T8T8 54\n\
\QKK77 830\n\
\KKKJJ 210\n\
\9T9J9 383\n\
\6Q464 285\n\
\73257 159"






input_to_parts :: String -> [[String]]
input_to_parts s =  map (wordsWhen (==' ')) (wordsWhen (=='\n') s)



-- given input string, returns [bet] ordered by their score
-- (best scoring hand comes LAST)
get_ordered_bets :: String -> [Int]
get_ordered_bets input = map snd (
    sort (
      map line_to_score_and_bet (input_to_parts input)
    )
  )


-- retuns (((type_of_hand, value_of_hand), bet)
line_to_score_and_bet :: [String] -> ((Int,[Int]),Int)
line_to_score_and_bet [hand,bet_str] = (hand_to_score hand, (read bet_str :: Int))



-- returns (type_of_hand, value_of_hand)
hand_to_score :: String -> (Int,[Int])
hand_to_score s = (hand_to_type_handle_jokers s, hand_to_value s)


joker_replacements = "23456789TJQKA"

-- return the list of strings with chr in front of all strings
put_card_in_front_of :: [String] -> Char -> [String]
put_card_in_front_of xs chr = map ([chr]++) xs

expand_joker_hands :: String -> [String]
expand_joker_hands "" = [""]
expand_joker_hands ('J':str) = concat (map (put_card_in_front_of (expand_joker_hands str)) joker_replacements)
expand_joker_hands (chr:str) = put_card_in_front_of (expand_joker_hands str) chr


hand_to_type_handle_jokers :: String->Int
hand_to_type_handle_jokers hand = maximum (map hand_to_type (expand_joker_hands hand))



has_n_chars n charfreq = (snd charfreq) == n

-- returns which class of hands this hand falls into.
-- in the order (high card (0), one pair, two pair, three of a kind, 
-- full house, four of a kind, five of a kind (6))
hand_to_type::String -> Int
hand_to_type hand = 
  if (any (has_n_chars 5) card_freqs) then 6 else 
  if (any (has_n_chars 4) card_freqs) then 5 else
  if ((any (has_n_chars 3) card_freqs) && (any (has_n_chars 2) card_freqs)) then 4 else
  if (any (has_n_chars 3) card_freqs) then 3 else
  if ((length (filter (has_n_chars 2) card_freqs)) == 2) then 2 else --two pairs
  if (any (has_n_chars 2) card_freqs) then 1 else
  0 
  where card_freqs = stringCharFreqs hand

card_ordering = "J23456789TJQKA"
cardVal :: Char -> Int
cardVal c = case elemIndex c card_ordering of
   Just n -> n
   Nothing -> 0

-- return some kind of lexicographic ordering of a hand.
hand_to_value::String -> [Int]
hand_to_value s =  map cardVal s





prod_sum_reduce :: [(Int,Int)] -> Int
prod_sum_reduce ((a,b):xs) = a*b+(prod_sum_reduce xs)
prod_sum_reduce [] = 0


process :: String -> Int
process input = prod_sum_reduce (zip [1..] (get_ordered_bets input))



main = do
    print (show (process test_input))
    print (show (process real_input))
    -- print (show (expand_joker_hands "ABCDE"))
    -- print (show (expand_joker_hands "JBCDE"))
    -- print (show (expand_joker_hands "ABCJE"))
    -- print (show (expand_joker_hands "ABJCJ"))


