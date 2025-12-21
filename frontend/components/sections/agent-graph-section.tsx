import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { GitBranch } from "lucide-react"
import Image from "next/image"

export function AgentGraphSection() {
  return (
    <div className="space-y-4">
      <div className="flex items-center gap-2 mb-4">
        <GitBranch className="h-5 w-5 text-primary" />
        <h3 className="text-lg font-semibold text-foreground">Agent Reasoning Graph</h3>
      </div>

      <Card className="border-border">
        <CardHeader>
          <CardTitle className="text-base">LangGraph Flow Diagram</CardTitle>
          <CardDescription>
            Visual representation of the AI agent's decision-making process and state transitions
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="relative w-full aspect-video bg-muted/30 rounded-lg overflow-hidden">
            <Image
              src="/artifacts/graphs/quiz_agent_graph.jpg"
              alt="Agent Reasoning Graph showing the LangGraph flow"
              fill
              className="object-contain p-4"
              priority
            />
          </div>
          <p className="text-xs text-muted-foreground mt-4">
            This graph shows how the autonomous agent processes your educational content through multiple stages, making
            decisions and validating results at each step.
          </p>
        </CardContent>
      </Card>
    </div>
  )
}
