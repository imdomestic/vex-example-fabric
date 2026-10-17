package com.imdomestic.vex.example;

import com.mojang.brigadier.CommandDispatcher;
import net.minecraft.commands.CommandSourceStack;
import net.minecraft.SharedConstants;
import net.minecraft.server.Bootstrap;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

final class ExampleCommandTest {
    @Test void brigadierRecognizesCommandAndRejectsTrailingArguments() {
        SharedConstants.tryDetectVersion();
        Bootstrap.bootStrap();
        CommandDispatcher<CommandSourceStack> dispatcher = new CommandDispatcher<>();
        dispatcher.register(ExampleCommand.command());
        var parsed = dispatcher.parse("vexexample", null);
        assertTrue(parsed.getExceptions().isEmpty());
        assertFalse(parsed.getReader().canRead());
        assertNotNull(parsed.getContext().getCommand());
        assertTrue(dispatcher.parse("vexexample unexpected", null).getReader().canRead());
        assertTrue(dispatcher.parse("anothercommand", null).getReader().canRead());
    }
}
