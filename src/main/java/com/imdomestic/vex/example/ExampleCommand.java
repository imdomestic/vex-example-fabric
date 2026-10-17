package com.imdomestic.vex.example;

import com.mojang.brigadier.builder.LiteralArgumentBuilder;
import net.minecraft.commands.CommandSourceStack;
import net.minecraft.commands.Commands;
import net.minecraft.network.chat.Component;

final class ExampleCommand {
    static LiteralArgumentBuilder<CommandSourceStack> command() {
        return Commands.literal("vexexample").executes(context -> {
            context.getSource().sendSuccess(() -> Component.literal("Vex Example v2"), false);
            return 1;
        });
    }
}
