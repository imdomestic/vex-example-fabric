package com.imdomestic.vex.example;

import net.fabricmc.api.DedicatedServerModInitializer;
import net.fabricmc.fabric.api.command.v2.CommandRegistrationCallback;

public final class VexExample implements DedicatedServerModInitializer {
    @Override public void onInitializeServer() {
        CommandRegistrationCallback.EVENT.register((dispatcher, registry, environment) -> dispatcher.register(ExampleCommand.command()));
    }
}
