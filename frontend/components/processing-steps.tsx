"use client"

import { Card, CardContent } from "@/components/ui/card"
import { CheckCircle2, Circle, Loader2 } from "lucide-react"

interface ProcessingStepsProps {
  currentStep: number
}

const STEPS = [
  { label: "Extracting concepts", description: "Analyzing text for key educational concepts" },
  { label: "Building hierarchy", description: "Organizing concepts into knowledge structure" },
  { label: "Generating quiz", description: "Creating quiz questions from concepts" },
  { label: "Ranking difficulty", description: "Assigning difficulty levels to questions" },
  { label: "Validation", description: "Validating quiz quality and coherence" },
]

export function ProcessingSteps({ currentStep }: ProcessingStepsProps) {
  return (
    <Card className="border-border">
      <CardContent className="pt-6">
        <div className="space-y-6">
          <div className="text-center mb-8">
            <h2 className="text-xl font-semibold text-foreground mb-2">Processing Your Content</h2>
            <p className="text-sm text-muted-foreground">The AI agent is analyzing your educational content</p>
          </div>

          <div className="space-y-4 max-w-2xl mx-auto">
            {STEPS.map((step, index) => {
              const isComplete = index < currentStep
              const isCurrent = index === currentStep
              const isPending = index > currentStep

              return (
                <div
                  key={step.label}
                  className={`flex items-start gap-4 p-4 rounded-lg border transition-colors ${
                    isCurrent
                      ? "bg-primary/5 border-primary"
                      : isComplete
                        ? "bg-muted/50 border-border"
                        : "bg-card border-border/50"
                  }`}
                >
                  <div className="mt-0.5">
                    {isComplete && <CheckCircle2 className="h-5 w-5 text-accent" />}
                    {isCurrent && <Loader2 className="h-5 w-5 text-primary animate-spin" />}
                    {isPending && <Circle className="h-5 w-5 text-muted-foreground" />}
                  </div>
                  <div className="flex-1 min-w-0">
                    <p
                      className={`text-sm font-medium ${
                        isCurrent ? "text-primary" : isComplete ? "text-foreground" : "text-muted-foreground"
                      }`}
                    >
                      {step.label}
                    </p>
                    <p className="text-xs text-muted-foreground mt-0.5">{step.description}</p>
                  </div>
                </div>
              )
            })}
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
