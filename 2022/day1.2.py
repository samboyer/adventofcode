print(
    sum(
        sorted(
            sum(
                map(
                    int,
                    e.strip().split('\n')
                )
            )
            for e in open('i/1').read().split('\n\n')
        )[-3:]
    )
)
