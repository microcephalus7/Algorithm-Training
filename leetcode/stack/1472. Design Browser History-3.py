# one stack

class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.frwd = 0  # number of urls which will be displayed after passing forward
        self.cur = 0  # current displayed url's index

    def visit(self, url: str) -> None:
        # previous history(urls which will be displayed after forward) will be deleted
        self.arr = self.arr[:self.cur+1]
        self.arr.append(url)
        self.frwd = 0  # there is no forward history and set to 0
        self.cur += 1  # current index is increased

    def back(self, n: int) -> str:
        if n <= self.cur:  # switch to the page which is n steps back
            self.cur -= n
            self.frwd += n
        else:   # switch to home page when n is greater than possible back steps
            self.cur = 0  # current index is set to homepage
            # the number of remaining pages for which there is access to the switch
            self.frwd = len(self.s)-1
        return self.arr[self.cur]  # returns the current page

    def forward(self, n: int) -> str:
        if n <= self.frwd:  # switch to the page which is n steps forward
            self.frwd -= n
            self.cur += n
        else:    # switch to the last page when n is greater than possible forward steps
            # current index is set to last page's index
            self.cur = len(self.s)-1
            self.frwd = 0  # there is no else forward page
        return self.arr[self.cur]  # returns the current page
