

default: build run
run: ./bin/Debug/net5.0/Chess.dll
	dotnet ./bin/Debug/net5.0/Chess.dll

build: Program.cs ChessPlayer.cs ChessMatch.cs
	dotnet build

clean:
	rm -r obj bin
