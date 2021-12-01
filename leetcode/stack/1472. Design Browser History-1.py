# two stack

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curPage = homepage
        self.prevStack = []
        self.forwardStack = []

    def visit(self, url: str) -> None:

        self.prevStack.append(self.curPage)
        self.forwardStack = []
        self.curPage = url

    def back(self, steps: int) -> str:

        possible = min(steps, len(self.prevStack))

        while possible:  # Step 0
            self.forwardStack.append(self.curPage)
            self.curPage = self.prevStack.pop()
            possible -= 1  # Step 3

        return self.curPage

    def forward(self, steps: int) -> str:

        possible = min(steps, len(self.forwardStack))

        while possible:  # Step 0
            self.prevStack.append(self.curPage)  # Step 1
            self.curPage = self.forwardStack.pop()
            possible -= 1  # Step 3

        return self.curPage
