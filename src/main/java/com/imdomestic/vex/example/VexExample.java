package com.imdomestic.vex.example;

import net.fabricmc.api.DedicatedServerModInitializer;
import net.fabricmc.fabric.api.command.v2.CommandRegistrationCallback;
import org.slf4j.LoggerFactory;

public final class VexExample implements DedicatedServerModInitializer {
    static final String PREVIEW_MARKER = "Vex Example CI preview 1";

    @Override public void onInitializeServer() {
        LoggerFactory.getLogger("vex-example").info(PREVIEW_MARKER);
        CommandRegistrationCallback.EVENT.register((dispatcher, registry, environment) -> dispatcher.register(ExampleCommand.command()));
    }
}
