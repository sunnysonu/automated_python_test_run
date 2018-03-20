import importlib

def test_right_rotations(package):
    score = 0
    try:
        module = importlib.import_module(".problem1", package = package)
        try:
            if(module.get_right_rotations(None, None) == -1):
                score += 1
        except:
            pass

        try:
            if(module.get_right_rotations(None, "abcd") == -1):
                score += 1
        except:
            pass

        try:
            if(module.get_right_rotations("abcd", "acbd") == -1):
                score += 4
        except:
            pass

        try:
            if(module.get_right_rotations("abcd", "cdab") == 2):
                score += 5
        except:
            pass

        try:
            if(module.get_right_rotations("aeiou", "aeiou") == 0):
                score += 4
        except:
            pass
    except ModuleNotFoundError:
        pass

    return score

def test_custom_base5(package):
    score = 0
    try:
        module = importlib.import_module(".problem2", package = package)
        score = 0
        try:
            if(module.to_custom_base5(0) == "a"):
                print("passed", score)
                score += 2
        except:
            pass

        try:
            if(module.to_custom_base5(1001) == "bdaab"):
                print("passed1")
                score +=5
        except:
            pass

        try:
            if(module.to_custom_base5(-1001) == "-bdaab"):
                print("passed2")
                score += 5
        except:
            pass

        try:
            module.to_custom_base5(3.2)
        except TypeError:
            print("passed3")
            score += 3

        try:
            if(module.from_custom_base5(" bdeab ") == 1101):
                print("passed1")
                score += 3
        except:
            pass

        try:
            if(module.from_custom_base5(" -bdeab ") == -1101):
                print("passed1")
                score += 3
        except:
            pass

        try:
            if(module.from_custom_base5(" +bdeab ") == 1101):
                print("passed1")
                score += 3
        except:
            pass

        try:
            if(module.from_custom_base5("BDeab") == 1101):
                print("passed1")
                score += 3
        except:
            pass

        try:
            module.from_custom_base5("BDhello")
        except ValueError:
            print("passed4")
            score += 3
        except:
            pass


        try:
            module.from_custom_base5("bde-ab")
        except ValueError:
            print("passed1")
            score += 3
        except:
            pass

        try:
            module.from_custom_base5(10)
        except TypeError:
            print("passed1")
            score += 2
        except:
            pass
    except ModuleNotFoundError:
        pass

    return score

def test_top_chars(package):
    score = 0
    try:
        module = importlib.import_module(".problem6", package = package)

        try:
            module.top_chars(None, 10)
        except TypeError:
            score += 1

        try:
            module.top_chars("hello", "w")
        except TypeError:
            score += 1

        try:
            module.top_chars("hello", -1)
        except ValueError:
            score += 1

        try:
            if(module.top_chars("acceeeffff", 2) == [("f", 4), ("e", 3)]):
                score += 8
        except:
            pass

        try:
            if(module.top_chars('ccggggeeff', 3) == [('g', 4), ('f', 2), ('e', 2)]):
                score += 8
        except:
            pass

        try:
            if(module.top_chars('FFggggeeff', 10) == [('g', 4), ('f', 2), ('e', 2), ('F', 2)]):
                score += 6
        except:
            pass
    except ModuleNotFoundError:
        pass

    return score

def test_factorize_number(package):
    score = 0
    try:
        module = importlib.import_module(".problem17", package = package)

        try:
            if(module.factorize_number(1) == []):
                score += 2
        except:
            pass

        try:
            if(module.factorize_number(6010) == [(2, 1), (5, 1), (601, 1)]):
                score += 5
        except:
            pass

        try:
            if(module.factorize_number(7865228921869442) == [(2, 1), (7919, 4)]):
                score += 10
        except:
            pass

        try:
            module.factorize_number(-10)
        except ValueError:
            score += 3

        try:
            module.factorize_number(3.2)
        except TypeError:
            score += 5
    except ModuleNotFoundError:
        pass
    return score

def test_get_lcm(package):
    score = 0
    try:
        module = importlib.import_module(".problem18", package = package)

        try:
            if(module.get_lcm([], [(2, 5)]) == [(2, 5)]):
                score += 2
        except:
            pass

        try:
            if(module.get_lcm([], []) == []):
                score += 3
        except:
            pass

        try:
            if(module.get_lcm([(2, 1), (5, 2), (7, 2)], [(2, 2), (3, 1), (17, 2)]) == [(2, 2), (3, 1), (5, 2), (7, 2), (17, 2)]):
                score += 5
        except:
            pass

        try:
            if(module.get_lcm([(2, 1), (19, 1), (7919, 4)], [(2, 2), (17, 1), (2687, 4)]) == [(2, 2), (17, 1), (19, 1), (2687, 4), (7919, 4)]):
                score += 15
        except:
            pass
    except ModuleNotFoundError:
        pass
    return score

def test_get_hcf(package):
    score = 0
    try:
        module = importlib.import_module(".problem19", package = package)
        try:
            if(module.get_hcf([], [(2, 5)]) == []):
                score += 2
        except:
            pass

        try:
            if(module.get_hcf([], []) == []):
                score += 3
        except:
            pass

        try:
            if(module.get_hcf([(2, 3), (3, 3), (11, 1)], [(5, 2)]) == []):
                score += 5
        except:
            pass

        try:
            if(module.get_hcf([(2, 3), (5, 3), (17, 2)], [(2, 1), (3, 5), (5, 2), (19, 1)]) == [(2, 1), (5, 2)]):
                score += 5
        except:
            pass

        try:
            if(module.get_hcf([(2, 1), (11, 3), (19, 2), (7919, 4)], [(2, 2), (7, 1), (19, 1), (2687, 4)]) == [(2, 1), (19, 1)]):
                score += 10
        except:
            pass
    except ModuleNotFoundError:
        pass

    return score

def test_top_earners(package):
    score = 0
    try:
        module = importlib.import_module(".problem20", package = package)
    except ModuleNotFoundError:
        return score
    try:
        module.top_earners("referral1.txt", -1, 10)
    except ValueError:
        score += 2

    try:
        module.top_earners('referral1.txt', 3, -2)
    except ValueError:
        score += 3
    try:
        if(module.top_earners('referral1.txt', 1, 1) == [('A', 200)]):
            score += 5
    except:
        pass

    try:
        if(module.top_earners('referral1.txt', 2, 2) == [('A', 300), ('B', 200)]):
            score += 5
    except:
        pass

    try:
        if(module.top_earners('referral1.txt', 3, 10) == [('A', 350), ('B', 300), ('P', 200)]):
            score += 10
    except:
        pass

    return score
