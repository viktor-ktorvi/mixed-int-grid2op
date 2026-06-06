import grid2op


def main() -> None:
    env_name = "l2rpn_case14_sandbox"
    env = grid2op.make(env_name)

    obs = env.reset()
    print(obs)

    net = env.backend._grid
    print(net)


if __name__ == "__main__":
    main()
