print(
    max(
        map(
            lambda e:sum(
                map(
                    int,
                    e.strip().split('\n')
                )
            ),
            open('i/1').read().split('\n\n')
        )
    )
)
