print(
    max(
        sum(
            map(
                int,
                e.split('\n')
            )
        ) for e in open('i/1').read()[:-1].split('\n\n')
    )
)
